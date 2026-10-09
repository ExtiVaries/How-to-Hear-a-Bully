#!/usr/bin/env python3
"""Review-gated, atomic timeline updates. Standard library only; no network writes."""
import argparse
import copy
import datetime as dt
import hashlib
import ipaddress
import json
import os
from pathlib import Path
import re
import tempfile
import uuid
from contextlib import contextmanager
from urllib.parse import urlparse, parse_qsl


class Invalid(ValueError):
    pass


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def date(value):
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
        raise Invalid('Expected ISO calendar date')
    try:
        dt.date.fromisoformat(value)
    except (ValueError, TypeError):
        raise Invalid('Expected ISO calendar date')


def bounded_date(value, today):
    date(value)
    if value > today: raise Invalid('Recorded and check dates cannot be in the future')


def public_url(value):
    if not isinstance(value, str): raise Invalid('Source URL must be text')
    try:
        parsed = urlparse(value); host = (parsed.hostname or '').lower().rstrip('.')
        port = parsed.port
    except ValueError:
        raise Invalid('Invalid source URL')
    if parsed.scheme != 'https' or not host or parsed.username or parsed.password or port not in (None,443) or 'notion' in host or any(c.isspace() for c in value):
        raise Invalid('Evidence must use public HTTPS URLs without credentials')
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        address = None
    if address and not address.is_global:
        raise Invalid('Private or local evidence URL')
    if not address and ('.' not in host or host.endswith(('.local','.localhost','.internal','.lan','.home','.test','.invalid')) or host == 'localhost' or re.fullmatch(r'[0-9.]+',host)):
        raise Invalid('Private or local evidence URL')
    credential_keys = {'token','access_token','api_key','apikey','key','secret','password','auth','authorization','signature','sig','credential'}
    if any(key.lower().replace('-','_') in credential_keys or key.lower().startswith(('x_amz_','x-amz-')) for key,_ in parse_qsl(parsed.query,keep_blank_values=True)):
        raise Invalid('Credential-bearing source query')


def validate(data, today=None):
    today = today or dt.date.today().isoformat(); date(today)
    if not isinstance(data, dict) or data.get('schema_version') != 1 or not isinstance(data.get('events'), list) or not isinstance(data.get('history'), list):
        raise Invalid('Unsupported or incomplete schema')
    if not isinstance(data.get('coverage'),dict): raise Invalid('Missing coverage')
    date(data['coverage']['start']); date(data['coverage']['end'])
    if data['coverage']['end'] < data['coverage']['start']: raise Invalid('Coverage end precedes start')
    if data['coverage']['end'] > today: raise Invalid('Coverage cannot claim future recording')
    ids = set(); identities = set()
    required = ('series title scope action_type legal_status what_happened previous_position what_changed applies_now uncertainty update_trigger check_note').split()
    for event in data['events']:
        if not isinstance(event, dict): raise Invalid('Event must be an object')
        ident = event.get('id', '')
        if not isinstance(ident,str) or not re.fullmatch(r'us-[a-z0-9]+(?:-[a-z0-9]+)*', ident) or ident in ids:
            raise Invalid('Invalid or duplicate stable event ID')
        ids.add(ident)
        for key in required:
            if not isinstance(event.get(key), str) or not event[key].strip():
                raise Invalid(f'{ident}: missing {key}')
        for key in ('first_recorded', 'last_substantive_revision'):
            bounded_date(event[key],today)
        if event['last_substantive_revision'] < event['first_recorded']: raise Invalid('Revision precedes recording')
        if event.get('last_successful_source_check') is not None:
            bounded_date(event['last_successful_source_check'],today)
        for key in ('event_date', 'effective_date'):
            value = event.get(key)
            if value is None and key == 'effective_date':
                continue
            patterns = {'day': r'\d{4}-\d{2}-\d{2}', 'month': r'\d{4}-\d{2}', 'year': r'\d{4}'}
            if not isinstance(value, dict) or not isinstance(value.get('precision'),str) or not isinstance(value.get('value'),str) or not re.fullmatch(patterns.get(value.get('precision'), r'(?!)'), value.get('value', '')):
                raise Invalid(f'{ident}: invalid date precision')
            date(value['value'] + {'day':'', 'month':'-01', 'year':'-01-01'}[value['precision']])
            if key == 'event_date' and value['value'] + {'day':'', 'month':'-01', 'year':'-01-01'}[value['precision']] > today:
                raise Invalid('Event date cannot claim a future occurrence; use effective date for scheduled effects')
        if type(event.get('check_interval_days')) is not int or not 1 <= event['check_interval_days'] <= 365:
            raise Invalid(f'{ident}: invalid check interval')
        if not isinstance(event.get('jurisdiction'),list) or not event['jurisdiction'] or not all(isinstance(j,str) and j.strip() for j in event['jurisdiction']) or not isinstance(event.get('sources'),list) or not event['sources']:
            raise Invalid(f'{ident}: missing scope or evidence')
        if not isinstance(event.get('practical_effects'),list) or not isinstance(event.get('related_events'),list) or not all(isinstance(i,str) for i in event['related_events']):
            raise Invalid(f'{ident}: effects and related events must be lists')
        source_ids = set()
        for source in event['sources']:
            if not isinstance(source,dict) or not isinstance(source.get('id'),str) or source.get('id') in source_ids or not source.get('id'):
                raise Invalid(f'{ident}: duplicate source ID')
            source_ids.add(source['id'])
            public_url(source.get('url'))
            for key in ('title', 'publisher', 'locator', 'supports', 'version_note'):
                if not isinstance(source.get(key), str):
                    raise Invalid(f'{ident}: missing source {key}')
            if source.get('access') not in ('full', 'indexed', 'blocked'):
                raise Invalid(f'{ident}: invalid evidence access')
            for key in ('last_checked', 'document_date'):
                if source.get(key) is not None: bounded_date(source[key],today)
            if source.get('content_sha256') is not None and (not isinstance(source['content_sha256'],str) or not re.fullmatch(r'[0-9a-f]{64}',source['content_sha256'])):
                raise Invalid('Invalid stored source hash')
            if source.get('evidence_note') is not None and not isinstance(source['evidence_note'],str): raise Invalid('Evidence note must be text')
        complete = event.get('last_successful_source_check')
        if complete is not None and complete < event['last_substantive_revision']:
            raise Invalid('Complete check cannot precede the substantive revision it supports')
        if complete is not None and (any(s['access'] != 'full' or not s.get('last_checked') for s in event['sources']) or complete > min(s['last_checked'] for s in event['sources'])):
            raise Invalid('Complete check requires full sources checked on or after its date')
        identity = (event['series'], event['event_date']['value'], event['action_type'], tuple(sorted(s['url'] for s in event['sources'])))
        if identity in identities:
            raise Invalid('Duplicate event identity under different ID')
        identities.add(identity)
        for effect in event.get('practical_effects', []):
            if not isinstance(effect,dict) or effect.get('kind') not in ('documented','reported','measured','inference','forecast') or not isinstance(effect.get('text'),str) or not effect['text'].strip() or not isinstance(effect.get('source_ids'),list) or not effect['source_ids'] or not all(isinstance(i,str) for i in effect['source_ids']) or not set(effect['source_ids']) <= source_ids:
                raise Invalid(f'{ident}: unsupported practical effect')
    for event in data['events']:
        if not set(event.get('related_events', [])) <= ids:
            raise Invalid('Unknown related event')
    history_ids = set()
    for item in data['history']:
        if not isinstance(item,dict) or not isinstance(item.get('id'),str) or item.get('id') in history_ids or not item.get('id') or not isinstance(item.get('event_id'),str) or item.get('event_id') not in ids or item.get('kind') not in ('correction','development') or not isinstance(item.get('reason'),str) or not item['reason'].strip() or not isinstance(item.get('before'), dict):
            raise Invalid('Invalid correction history')
        history_ids.add(item['id']); bounded_date(item['date'],today)
    return data


def read(path):
    return validate(json.loads(Path(path).read_text(encoding='utf-8')))


@contextmanager
def lock(path):
    lockpath = Path(str(path) + '.lock')
    token = uuid.uuid4().hex
    try:
        fd = os.open(lockpath, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        raise Invalid(f'Writer lock exists: {lockpath}; inspect owner, never steal automatically')
    try:
        with os.fdopen(fd, 'w') as stream:
            json.dump({'pid':os.getpid(), 'started':dt.datetime.now(dt.timezone.utc).isoformat(), 'token':token}, stream)
        yield
    finally:
        try:
            owner = json.loads(lockpath.read_text(encoding='utf-8'))
            if not isinstance(owner,dict) or owner.get('token') != token:
                raise Invalid('Writer lock ownership changed; replacement lock retained')
            lockpath.unlink()
        except (OSError,json.JSONDecodeError) as error:
            raise Invalid('Writer lock changed or missing; inspect owner before recovery') from error


def atomic(path, data):
    path = Path(path)
    fd, name = tempfile.mkstemp(prefix='.timeline-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as stream:
            json.dump(data, stream, ensure_ascii=False, indent=2); stream.write('\n'); stream.flush(); os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name): os.unlink(name)


def substantive(event):
    event = copy.deepcopy(event)
    for key in ('last_successful_source_check','check_note','last_substantive_revision'):
        event.pop(key, None)
    for source in event['sources']:
        source.pop('last_checked', None); source.pop('access', None)
        source.pop('content_sha256',None); source.pop('evidence_note',None)
    return event


def prepare(old, candidate, reason, kind, today):
    date(today)
    if today > dt.date.today().isoformat(): raise Invalid('Update date cannot be in the future')
    validate(old,today); validate(candidate,today)
    if not isinstance(reason,str) or (candidate != old and not reason.strip()): raise Invalid('Every changed candidate requires an editorial review reason')
    result = copy.deepcopy(candidate)
    if candidate['history'] != old['history']:
        raise Invalid('Candidate must preserve immutable history exactly; engine appends it')
    before = {e['id']:e for e in old['events']}; after = {e['id']:e for e in result['events']}
    if not before.keys() <= after.keys():
        raise Invalid('Events cannot be silently deleted')
    for ident, previous in before.items():
        current = after[ident]
        if current['first_recorded'] != previous['first_recorded']:
            raise Invalid('First recorded date is immutable')
        old_sources={s['id']:s for s in previous['sources']}
        for source in current['sources']:
            prior=old_sources.get(source['id'])
            if prior and prior.get('last_checked') and (not source.get('last_checked') or source['last_checked'] < prior['last_checked']):
                raise Invalid('Source check dates cannot move backward')
        hash_amended = any(old_sources.get(s['id'],{}).get('content_sha256') and s.get('content_sha256') != old_sources[s['id']]['content_sha256'] for s in current['sources'])
        if substantive(current) != substantive(previous) or hash_amended:
            if not reason.strip(): raise Invalid('Substantive amendments require editorial reason')
            current['last_substantive_revision'] = today
            current['last_successful_source_check'] = None
            record = {'event_id':ident,'date':today,'kind':kind,'reason':reason,'before':copy.deepcopy(previous)}
            record['id'] = ident + '-' + hashlib.sha256(json.dumps(record,sort_keys=True).encode()).hexdigest()[:12]
            result['history'].append(record)
        else:
            current['last_substantive_revision'] = previous['last_substantive_revision']
            prior_check=previous.get('last_successful_source_check')
            if prior_check and (not current.get('last_successful_source_check') or current['last_successful_source_check'] < prior_check):
                raise Invalid('Complete check dates cannot move backward on unchanged content')
    return validate(result,today)


def checks(data, report):
    validate(data)
    result = copy.deepcopy(data)
    if not isinstance(report, dict) or not set(report) <= {e['id'] for e in data['events']}:
        raise Invalid('Source report names unknown event')
    # Report explicitly lists each source actually read. HTTP success alone is not a source check.
    for event in result['events']:
        outcomes = report.get(event['id'], {})
        if not isinstance(outcomes, dict) or not set(outcomes) <= {s['id'] for s in event['sources']}:
            raise Invalid('Source report names unknown source')
        for source in event['sources']:
            outcome = outcomes.get(source['id'], {})
            if not isinstance(outcome,dict) or (outcome and outcome.get('result') not in ('success','failed','amended')):
                raise Invalid('Malformed or unknown source-check result')
            if outcome.get('result') == 'success' and (not isinstance(outcome.get('evidence_note'),str) or not outcome['evidence_note'].strip() or not isinstance(outcome.get('content_sha256'),str) or not re.fullmatch(r'[0-9a-f]{64}', outcome['content_sha256'])):
                raise Invalid('Successful source check needs hash and comparison evidence')
            if outcome.get('result') == 'success' and outcome.get('evidence_note') and outcome.get('content_sha256') and re.fullmatch(r'[0-9a-f]{64}', outcome['content_sha256']):
                bounded_date(outcome['date'],dt.date.today().isoformat())
                if outcome['date'] < event['last_substantive_revision']:
                    raise Invalid('Source report predates current substantive revision; compare revised claims again')
                if source.get('content_sha256') and outcome['content_sha256'] != source['content_sha256']:
                    raise Invalid('Source bytes changed; amended source needs editorial review')
                if source.get('last_checked') and outcome['date'] < source['last_checked']:
                    raise Invalid('Source check dates cannot move backward')
                source['last_checked'] = outcome['date']
                source['access'] = 'full'
                source['content_sha256'] = outcome['content_sha256']
                source['evidence_note'] = outcome['evidence_note']
            elif outcome.get('result') == 'amended':
                raise Invalid('Amended source requires substantive candidate and editorial review')
        successful = [outcomes.get(s['id'], {}) for s in event['sources']]
        if successful and all(o.get('result') == 'success' and o.get('evidence_note') and re.fullmatch(r'[0-9a-f]{64}', o.get('content_sha256','')) for o in successful):
            event['last_successful_source_check'] = min(o['date'] for o in successful)
            event['check_note'] = 'All listed sources successfully checked against the entry; this is not independent factual certification.'
        elif outcomes:
            event['check_note'] = 'Partial or failed source check; the last complete successful check is retained.'
    return validate(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('validate','propose','apply','checks'))
    parser.add_argument('--record', default='docs/changes/timeline.json')
    parser.add_argument('--candidate'); parser.add_argument('--report'); parser.add_argument('--output')
    parser.add_argument('--baseline'); parser.add_argument('--review-sha256')
    parser.add_argument('--reason', default=''); parser.add_argument('--kind', choices=('correction','development'), default='development')
    parser.add_argument('--date', default=dt.date.today().isoformat())
    args = parser.parse_args(); date(args.date)
    try:
        old = read(args.record)
        if args.command == 'validate':
            print('Valid timeline; SHA256 ' + digest(args.record)); return
        if args.command == 'checks':
            result = checks(old, json.loads(Path(args.report).read_text(encoding='utf-8')))
        elif args.command == 'propose':
            result = prepare(old, read(args.candidate), args.reason, args.kind, args.date)
        else:
            result = read(args.candidate)
        if args.command in ('propose','checks'):
            if not args.output or Path(args.output).resolve() == Path(args.record).resolve(): raise Invalid('Proposal output must differ from canonical record')
            atomic(args.output, result)
            print('Draft candidate ' + args.output + '; SHA256 ' + digest(args.output) + '; baseline ' + digest(args.record)); return
        with lock(args.record):
            # Hash and parse exactly the same bytes under the writer lock.
            record_bytes=Path(args.record).read_bytes(); candidate_bytes=Path(args.candidate).read_bytes()
            if not args.review_sha256 or hashlib.sha256(candidate_bytes).hexdigest() != args.review_sha256: raise Invalid('Exact reviewed candidate SHA256 required')
            previous = validate(json.loads(record_bytes.decode('utf-8')))
            reviewed = validate(json.loads(candidate_bytes.decode('utf-8')))
            if reviewed == previous:
                print('Unchanged reviewed record; no write'); return
            if not args.baseline or hashlib.sha256(record_bytes).hexdigest() != args.baseline: raise Invalid('Baseline changed; rebase and review again')
            unprepared = copy.deepcopy(reviewed); unprepared['history'] = copy.deepcopy(previous['history'])
            result = prepare(previous, unprepared, args.reason, args.kind, args.date)
            if result != reviewed: raise Invalid('Reviewed history does not match computed immutable revision')
            if Path(args.record).read_bytes() != record_bytes: raise Invalid('Canonical record changed outside lock; no write')
            atomic(args.record, result)
            print('Reviewed local record applied; build and site validation still required before PR')
    except (Invalid, KeyError, TypeError, UnicodeError, OSError, json.JSONDecodeError) as error:
        parser.exit(1, 'Update rejected; canonical record retained: ' + str(error) + '\n')


if __name__ == '__main__':
    main()
