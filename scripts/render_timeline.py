"""Static HTML and Markdown editions from the same validated timeline record."""
from datetime import date, timedelta
from html import escape
import json

from update_timeline import validate


def due(event):
    checked = event['last_successful_source_check']
    return (date.fromisoformat(checked) + timedelta(days=event['check_interval_days'])).isoformat() if checked else None


def render(data):
    validate(data)
    titles = {event['id']: event['title'] for event in data['events']}
    series = sorted({event['series'] for event in data['events']})
    e = escape
    review_notice = 'No recurring timeline check is active; suggested manual review dates flag when another comparison is needed, not a promise that it is scheduled or has happened.'
    controls = '''<form id="timeline-filters" class="wc-filters" hidden role="search" aria-label="Filter timeline">
<div><label for="timeline-query">Search entries</label><input id="timeline-query" type="search" placeholder="Topic, place, action…"></div>
<div><label for="timeline-series">Follow a history</label><select id="timeline-series"><option value="">All histories</option>'''
    controls += ''.join(f'<option value="{e(item)}">{e(item.replace("-", " "))}</option>' for item in series)
    controls += '''</select></div><button type="reset">Clear filters</button>
<p id="timeline-count" role="status" aria-live="polite" aria-atomic="true"></p></form>
<noscript><p>All entries and sources are available below. Use your browser's Find command to search the page.</p></noscript>'''
    cards, md = [], ['# U.S. timeline: What actually changed?', '', '[Read the guide](guide.md) · [Methods and source notes](methodology.md)', '',
                     'Coverage: ' + data['coverage']['start'] + ' through ' + data['coverage']['end'] + '. ' + data['coverage']['description'], '', data['coverage']['selection'], '', review_notice, '']
    for event in sorted(data['events'], key=lambda item: (item['event_date']['value'], item['id']), reverse=True):
        ident = event['id']
        checks = event['last_successful_source_check'] or 'No complete check; see access limits'
        next_due = due(event)
        fresh = f'<p class="pg-meta wc-fresh" data-checked="{event["last_successful_source_check"] or ""}" data-due="{next_due or ""}">Last complete source check: {e(checks)}.'
        fresh += f' Suggested manual review date: {next_due} ({event["check_interval_days"]} days).' if next_due else ' Complete check needed.'
        if not next_due:
            fresh += f' Review interval after a complete check: {event["check_interval_days"]} days.'
        fresh += '</p>'
        effects = ''.join(f'<li><strong>{e(effect["kind"].capitalize())}:</strong> {e(effect["text"])} ' + ' · '.join(f'<a href="#{ident}-source-{e(source_id)}">Evidence {index}</a>' for index, source_id in enumerate(effect['source_ids'], 1)) + '</li>' for effect in event['practical_effects'])
        if not effects:
            effects = '<li>No practical effect established by the listed sources; this does not establish an absence of consequences.</li>'
        sources = ''
        for source in event['sources']:
            sources += f'''<li id="{ident}-source-{e(source['id'])}"><a href="{e(source['url'], quote=True)}">{e(source['title'])}</a> — {e(source['publisher'].rstrip('. '))}. <strong>Locator:</strong> {e(source['locator'].rstrip('. '))}. <strong>Supports:</strong> {e(source['supports'].rstrip('. '))}. <strong>Access:</strong> {e(source['access'])}; last successful comparison: {e(source['last_checked'] or 'not established')}. {e(source['version_note'])}</li>'''
        related = ' · '.join(f'<a href="#{e(other)}">{e(titles[other])}</a>' for other in event['related_events'])
        effective = event['effective_date']
        effective_text = f'{effective["value"]} ({effective["precision"]} precision)' if effective else 'Not established / not applicable; see status'
        revisions = [item for item in data['history'] if item['event_id'] == ident]
        revision_link = ''.join(f'<p><a href="#{e(item["id"])}">{e(item["kind"].capitalize())} — {item["date"]}</a></p>' for item in revisions)
        cards.append(f'''<section class="wc-event" id="{ident}" data-series="{e(event['series'])}">
<p class="pg-eyebrow">{event['event_date']['value']} · {e(event['action_type'].replace('-', ' '))}</p>
<h2><a href="#{ident}">{e(event['title'])}</a></h2>
<p><strong>What happened:</strong> {e(event['what_happened'])}</p>
<p><strong>What changed:</strong> {e(event['what_changed'])}</p>
<p><strong>Scope:</strong> {e(event['scope'])}</p>
<p><strong>Legal / procedural status:</strong> {e(event['legal_status'])}</p>
<p><strong>What applies now:</strong> {e(event['applies_now'])}</p>
<p class="wc-effects-label"><strong>Practical consequences</strong></p><ul class="wc-effects">{effects}</ul>
{fresh}{revision_link}
<details><summary>Previous position, uncertainties, dates, and sources</summary>
<p><strong>Previously:</strong> {e(event['previous_position'])}</p>
<p><strong>Unresolved:</strong> {e(event['uncertainty'])}</p>
<p><strong>Update when:</strong> {e(event['update_trigger'])}</p>
<dl class="wc-dates"><dt>Event date / precision</dt><dd>{event['event_date']['value']} / {event['event_date']['precision']}</dd>
<dt>First recorded here</dt><dd>{event['first_recorded']}</dd><dt>Last substantive revision</dt><dd>{event['last_substantive_revision']}</dd>
<dt>Effective date</dt><dd>{e(effective_text)}</dd><dt>Jurisdiction</dt><dd>{e(', '.join(event['jurisdiction']))}</dd></dl>
<p class="pg-meta">{e(event['check_note'])}</p>
<h3>Public sources and limits</h3><ol class="wc-sources">{sources}</ol></details>
<p class="wc-related"><strong>Follow this history:</strong> {related or 'No related entry yet.'}</p></section>''')
        md += [f'## {event["title"]} {{#{ident}}}', '', f'Event: {event["event_date"]["value"]} ({event["event_date"]["precision"]} precision). Action: {event["action_type"]}.', '']
        for label, key in [('What happened','what_happened'),('Previously','previous_position'),('What changed','what_changed'),('Scope','scope'),('Legal / procedural status','legal_status'),('What applies now','applies_now')]:
            md += [f'**{label}:** {event[key]}', '']
        for effect in event['practical_effects']:
            md += [f'**{effect["kind"].capitalize()} effect:** {effect["text"]}', '']
        md += [f'**Unresolved:** {event["uncertainty"]}', '', f'**Update when:** {event["update_trigger"]}', '',
               f'First recorded: {event["first_recorded"]}. Last substantive revision: {event["last_substantive_revision"]}. Last complete source check: {checks}. Effective: {effective_text}. Jurisdiction: {", ".join(event["jurisdiction"])}. Suggested manual review date: {next_due or "complete check needed"}.', '', event['check_note'], '', '### Public sources', '']
        for source in event['sources']:
            md += [f'- [{source["title"]}]({source["url"]}) — {source["publisher"].rstrip(". ")}. Locator: {source["locator"].rstrip(". ")}. Supports: {source["supports"].rstrip(". ")}. Access: {source["access"]}; last comparison: {source["last_checked"] or "not established"}. {source["version_note"]}']
        related_md = ' · '.join(f'[{titles[other]}](#{other})' for other in event['related_events'])
        md += ['', '**Follow this history:** ' + (related_md or 'No related entry yet.'), '']
    history = '<section id="correction-history"><h2>Corrections and substantive revisions</h2>'
    md += ['## Corrections and substantive revisions {#correction-history}', '']
    if not data['history']:
        history += '<p>Initial edition: no previous public version and no public corrections yet. Test fixtures are excluded.</p>'
        md += ['Initial edition: no previous public version and no public corrections yet. Test fixtures are excluded.', '']
    for item in data['history']:
        history += f'<section id="{e(item["id"])}"><h3>{e(item["kind"].capitalize())}: {e(titles[item["event_id"]])}</h3><p>{item["date"]} — {e(item["reason"])}</p><p><a href="#{e(item["event_id"])}">Current event</a></p><details><summary>Earlier entry preserved in full</summary><pre>{e(json.dumps(item["before"], ensure_ascii=False, indent=2))}</pre></details></section>'
        md += [f'### {item["kind"].capitalize()}: {titles[item["event_id"]]} {{#{item["id"]}}}', '', item['date'] + ' — ' + item['reason'], '', f'[Current event](#{item["event_id"]})', '', '```json', json.dumps(item['before'], ensure_ascii=False, indent=2), '```', '']
    history += '</section>'
    body = f'''<main id="main-content" class="pg-reading wc-timeline"><header><p class="pg-eyebrow">Selected U.S. developments</p><h1>What actually changed?</h1><p>A running timeline of decisions, capacity, and consequences.</p><p><a href="./">Read the guide</a> · <a href="methodology.html">Methods and source notes</a> · <a href="timeline.json">Public JSON</a></p></header>
<p><strong>Coverage:</strong> {data['coverage']['start']} through {data['coverage']['end']}. {e(data['coverage']['description'])}</p><p>{e(data['coverage']['selection'])}</p>
<p>Entry dates describe specific checks. {e(review_notice)} Read the current-position and access notes before relying on an entry. Related links preserve the sequence; this is a curated record.</p>
{controls}<div id="timeline-events">{''.join(cards)}</div><p id="timeline-empty" hidden>No matching entries. Clear the filters to see the full history.</p>{history}<p class="pg-endlinks"><a href="./">Guide</a> · <a href="methodology.html#corrections">Report a correction</a> · <a href="../docs/changes/timeline.md">Markdown edition</a></p></main>'''
    return body, '\n'.join(md), json.dumps(data, ensure_ascii=False, indent=2) + '\n'
