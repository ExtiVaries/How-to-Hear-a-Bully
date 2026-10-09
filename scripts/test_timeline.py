"""Run with python scripts/test_timeline.py; small disposable fixtures only."""
import copy
import json
from pathlib import Path
import tempfile
import subprocess
import sys
import unittest
import update_timeline as engine
import render_timeline


def fixture():
    event = {key:'Evidence-based text' for key in ('series title scope action_type legal_status what_happened previous_position what_changed applies_now uncertainty update_trigger check_note').split()}
    event.update(id='us-test', event_date={'value':'2025-01-01','precision':'day'}, effective_date=None, first_recorded='2026-10-09',last_substantive_revision='2026-10-09',last_successful_source_check=None,check_interval_days=7,jurisdiction=['U.S. federal'],practical_effects=[],related_events=[],sources=[{'id':'s1','title':'Order','url':'https://example.gov/order','publisher':'Court','locator':'Page 1','supports':'Holding','last_checked':None,'access':'blocked','document_date':'2025-01-01','version_note':'Original'}])
    return {'schema_version':1,'coverage':{'start':'2025-01-01','end':'2026-10-09'},'events':[event],'history':[]}


class PipelineTests(unittest.TestCase):
    def test_renderer_empty_history_and_source_punctuation_match(self):
        data=fixture(); data['coverage'].update(description='Selected developments.',selection='Illustrative selection.')
        data['events'][0]['sources'][0].update(publisher='Court. ',locator='Page 1. ',supports='Holding. ')
        html,markdown,_=render_timeline.render(data)
        self.assertIn('<strong>Follow this history:</strong> No related entry yet.',html)
        self.assertIn('**Follow this history:** No related entry yet.',markdown)
        self.assertIn('— Court. Locator: Page 1. Supports: Holding. Access:',markdown)
        self.assertIn('— Court. <strong>Locator:</strong> Page 1. <strong>Supports:</strong> Holding.',html)
        self.assertNotIn('Court..',markdown)
        self.assertNotIn('Page 1. .',markdown)

    def test_complete_cli_cycle_and_baseline_race(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent, prefix='.test-') as temp:
            root=Path(temp); record=root/'record.json'; raw=root/'raw.json'; review=root/'review.json'
            old=fixture(); engine.atomic(record,old)
            candidate=copy.deepcopy(old); candidate['events'][0]['what_changed']='Bounded corrected scope'
            engine.atomic(raw,candidate)
            command=[sys.executable,str(Path(engine.__file__).resolve())]
            common=['--record',str(record),'--reason','Scope correction','--kind','correction','--date','2026-10-09']
            proposed=subprocess.run(command+['propose','--candidate',str(raw),'--output',str(review)]+common,capture_output=True,text=True)
            self.assertEqual(proposed.returncode,0,proposed.stderr)
            baseline=engine.digest(record); reviewed=engine.digest(review)
            applied=command+['apply','--candidate',str(review),'--baseline',baseline,'--review-sha256',reviewed]+common
            stale=subprocess.run(command+['apply','--candidate',str(review),'--baseline','0'*64,'--review-sha256',reviewed]+common,capture_output=True,text=True)
            self.assertNotEqual(stale.returncode,0); self.assertEqual(engine.read(record),old)
            result=subprocess.run(applied,capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual(len(engine.read(record)['history']),1)
            repeated=subprocess.run(applied,capture_output=True,text=True)
            self.assertEqual(repeated.returncode,0,repeated.stderr)
            self.assertEqual(len(engine.read(record)['history']),1)

    def test_duplicate_ids_and_identity(self):
        data=fixture(); data['events'].append(copy.deepcopy(data['events'][0]))
        with self.assertRaises(engine.Invalid): engine.validate(data)
        data['events'][1]['id']='us-test-two'
        with self.assertRaises(engine.Invalid): engine.validate(data)

    def test_overlap_lock(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent, prefix='.test-') as temp:
            path=Path(temp)/'record.json'
            with engine.lock(path):
                with self.assertRaises(engine.Invalid):
                    with engine.lock(path): pass
            self.assertFalse(Path(str(path)+'.lock').exists())

    def test_rerun_has_no_news(self):
        old=fixture()
        self.assertEqual(engine.prepare(old,old,'','development','2026-10-09'),old)
        self.assertEqual(engine.checks(old,{}),old)

    def test_correction_retains_original_and_reason(self):
        old=fixture(); changed=copy.deepcopy(old); changed['events'][0]['what_changed']='Corrected interpretation'
        result=engine.prepare(old,changed,'Original overstated scope','correction','2026-10-09')
        self.assertEqual(result['history'][0]['before'],old['events'][0])
        self.assertEqual(result['history'][0]['kind'],'correction')
        self.assertEqual(result['events'][0]['first_recorded'],'2026-10-09')
        self.assertEqual(engine.prepare(result,result,'','development','2026-10-09'),result)
        with self.assertRaises(engine.Invalid): engine.prepare(old,changed,'','correction','2026-10-09')

    def test_partial_check_retains_last_complete(self):
        old=fixture(); old['events'][0]['last_successful_source_check']='2026-10-01'
        old['events'][0]['first_recorded']='2026-10-01'
        old['events'][0]['last_substantive_revision']='2026-10-01'
        old['events'][0]['sources'][0].update(last_checked='2026-10-01',access='full')
        old['events'][0]['sources'].append(dict(old['events'][0]['sources'][0],id='s2',url='https://example.gov/other'))
        report={'us-test':{'s1':{'result':'success','date':'2026-10-09','content_sha256':'a'*64,'evidence_note':'Compared order paragraphs 1-2'},'s2':{'result':'failed'}}}
        result=engine.checks(old,report)
        self.assertEqual(result['events'][0]['last_successful_source_check'],'2026-10-01')
        self.assertEqual(result['events'][0]['last_substantive_revision'],'2026-10-01')
        self.assertEqual(len(result['events']),1)
        with self.assertRaises(engine.Invalid): engine.checks(old,{'us-test':{'s1':{'result':'amended'}}})

    def test_private_urls_and_credential_queries_rejected(self):
        urls=['https://127.0.0.1/private','https://192.168.1.1/x','https://[::1]/x','https://localhost/x','https://host.local/x','https://2130706433/x','https://example.gov/?api_key=secret','https://example.gov/?X-Amz-Signature=secret','https://notion.so/private']
        for url in urls:
            with self.subTest(url=url):
                data=fixture(); data['events'][0]['sources'][0]['url']=url
                with self.assertRaises(engine.Invalid): engine.validate(data)

    def test_malformed_shapes_and_outcomes_rejected(self):
        for value in ([],None,'bad'):
            with self.assertRaises(engine.Invalid): engine.validate(value)
        for field,value in [('practical_effects',{}),('jurisdiction','nationwide'),('sources',['oops']),('related_events',[{}]),('check_interval_days',True)]:
            data=fixture(); data['events'][0][field]=value
            with self.assertRaises(engine.Invalid): engine.validate(data)
        data=fixture(); data['coverage']['end']='2024-01-01'
        with self.assertRaises(engine.Invalid): engine.validate(data)
        for outcome in ([],{'result':'unknown'},{'result':'success','date':'2026-10-09'}):
            with self.assertRaises(engine.Invalid): engine.checks(fixture(),{'us-test':{'s1':outcome}})

    def test_fabricated_check_dates_and_unreviewed_changes_rejected(self):
        old=fixture(); candidate=copy.deepcopy(old)
        candidate['events'][0]['sources'][0].update(access='full',last_checked='2099-01-01')
        candidate['events'][0]['last_successful_source_check']='2099-01-01'
        with self.assertRaises(engine.Invalid): engine.prepare(old,candidate,'review','development','2026-10-09')
        candidate=copy.deepcopy(old); candidate['events'][0]['check_note']='Changed check note'
        with self.assertRaises(engine.Invalid): engine.prepare(old,candidate,'','development','2026-10-09')
        candidate=copy.deepcopy(old); candidate['events'][0]['last_successful_source_check']='2026-10-09'
        with self.assertRaises(engine.Invalid): engine.validate(candidate)
        candidate['events'][0]['sources'][0].update(access='full',last_checked='2026-10-01')
        with self.assertRaises(engine.Invalid): engine.validate(candidate)

    def test_hash_retention_amendment_detection_and_check_invalidation(self):
        outcome={'result':'success','date':'2026-10-09','content_sha256':'a'*64,'evidence_note':'Compared operative paragraphs'}
        checked=engine.checks(fixture(),{'us-test':{'s1':outcome}})
        self.assertEqual(checked['events'][0]['sources'][0]['content_sha256'],'a'*64)
        self.assertEqual(checked['events'][0]['last_successful_source_check'],'2026-10-09')
        with self.assertRaises(engine.Invalid): engine.checks(checked,{'us-test':{'s1':dict(outcome,content_sha256='b'*64)}})
        changed=copy.deepcopy(checked); changed['events'][0]['what_changed']='Revised scope'
        result=engine.prepare(checked,changed,'New interpretation','correction','2026-10-09')
        self.assertIsNone(result['events'][0]['last_successful_source_check'])
        self.assertEqual(result['history'][0]['before']['last_successful_source_check'],'2026-10-09')
        changed=copy.deepcopy(checked); changed['events'][0]['sources'][0]['content_sha256']='b'*64
        result=engine.prepare(checked,changed,'Amended public document','development','2026-10-09')
        self.assertEqual(len(result['history']),1)
        self.assertIsNone(result['events'][0]['last_successful_source_check'])

    def test_stale_report_cannot_restore_revised_entry_freshness(self):
        data=fixture()
        stale={'result':'success','date':'2026-10-08','content_sha256':'a'*64,'evidence_note':'Compared the previous interpretation'}
        with self.assertRaises(engine.Invalid): engine.checks(data,{'us-test':{'s1':stale}})
        data['events'][0]['sources'][0].update(access='full',last_checked='2026-10-08')
        data['events'][0]['last_successful_source_check']='2026-10-08'
        with self.assertRaises(engine.Invalid): engine.validate(data)

    def test_replaced_lock_is_preserved(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent, prefix='.test-') as temp:
            path=Path(temp)/'record.json'; lockpath=Path(str(path)+'.lock')
            with self.assertRaises(engine.Invalid):
                with engine.lock(path): lockpath.write_text(json.dumps({'token':'another-writer'}),encoding='utf-8')
            self.assertEqual(json.loads(lockpath.read_text())['token'],'another-writer')

    def test_invalid_candidate_preserves_last_good(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent, prefix='.test-') as temp:
            path=Path(temp)/'record.json'; old=fixture(); engine.atomic(path,old); before=path.read_bytes()
            bad=copy.deepcopy(old); bad['events'][0]['sources'][0]['url']='https://private.notion.so/secret'
            with self.assertRaises(engine.Invalid): engine.prepare(old,bad,'change','development','2026-10-09')
            self.assertEqual(path.read_bytes(),before)
            bad=copy.deepcopy(old); bad['events']=[]
            with self.assertRaises(engine.Invalid): engine.prepare(old,bad,'change','development','2026-10-09')

    def test_late_discovery_and_date_precision(self):
        data=fixture(); data['events'][0]['event_date']={'value':'2025-01','precision':'month'}
        engine.validate(data)
        self.assertNotEqual(data['events'][0]['event_date']['value'],data['events'][0]['first_recorded'])
        data['events'][0]['event_date']={'value':'2025-99','precision':'month'}
        with self.assertRaises(engine.Invalid): engine.validate(data)


if __name__=='__main__': unittest.main()
