import copy,unittest,json,subprocess,sys,tempfile
from pathlib import Path
from opsec_reports.core import ReportError,outcome
from backup_auditor.core import assess
NOW='2026-10-12T00:00:00Z'
def fixture():
 return {'schema_version':'backup-1.0','scope':'synthetic-backups','synthetic':True,'assets':[{'id':'synthetic-vault','excessive_read':False,'excessive_delete':False,'encrypted':True,'key_access_separate':True,'immutable':True,'immutability_verified':True,'restore':{'tested_at':'2026-10-01T00:00:00Z','result':'success','maximum_age_days':30}}]}
class BackupTests(unittest.TestCase):
 def test_positive(self):self.assertEqual(outcome(assess(fixture(),NOW)),0)
 def test_negative_each_control(self):
  for field,value,index in [('excessive_read',True,0),('excessive_delete',True,0),('encrypted',False,1),('key_access_separate',False,1),('immutable',False,2),('immutability_verified',False,2)]:
   d=fixture();d['assets'][0][field]=value;self.assertEqual(assess(d,NOW)['results'][index]['status'],'fail')
 def test_unknown_each_control(self):
  for field,index in [('excessive_read',0),('encrypted',1),('immutable',2)]:
   d=fixture();d['assets'][0][field]=None;self.assertEqual(assess(d,NOW)['results'][index]['status'],'not_tested')
 def test_invalid_types(self):
  for field in ['excessive_read','encrypted','immutable']:
   d=fixture();d['assets'][0][field]=1
   with self.assertRaises(ReportError):assess(d,NOW)
 def test_restore_failure(self):
  d=fixture();d['assets'][0]['restore']['result']='failure';self.assertEqual(assess(d,NOW)['results'][3]['status'],'fail')
 def test_restore_stale(self):
  d=fixture();d['assets'][0]['restore']['maximum_age_days']=10;self.assertEqual(assess(d,NOW)['results'][3]['status'],'fail')
 def test_restore_unknown(self):
  d=fixture();d['assets'][0]['restore']['tested_at']=None;self.assertEqual(assess(d,NOW)['results'][3]['status'],'not_tested')
 def test_restore_future(self):
  d=fixture();d['assets'][0]['restore']['tested_at']='2027-01-01T00:00:00Z'
  with self.assertRaises(ReportError):assess(d,NOW)
 def test_restore_invalid(self):
  d=fixture();d['assets'][0]['restore']['maximum_age_days']=True
  with self.assertRaises(ReportError):assess(d,NOW)
 def test_duplicates(self):
  d=fixture();d['assets']*=2
  with self.assertRaises(ReportError):assess(d,NOW)
 def test_empty(self):
  d=fixture();d['assets']=[]
  with self.assertRaises(ReportError):assess(d,NOW)

 def test_restore_exact_boundary(self):
  d=fixture();d['assets'][0]['restore']['tested_at']='2026-09-12T00:00:00Z';self.assertEqual(assess(d,NOW)['results'][3]['status'],'pass')
 def test_restore_one_second_stale(self):
  d=fixture();d['assets'][0]['restore']['tested_at']='2026-09-11T23:59:59Z';self.assertEqual(assess(d,NOW)['results'][3]['status'],'fail')
 def test_known_failure_overrides_unknown(self):
  d=fixture();d['assets'][0].update(encrypted=False,key_access_separate=None);self.assertEqual(assess(d,NOW)['results'][1]['status'],'fail')
 def test_asset_budget(self):
  d=fixture();a=copy.deepcopy(d['assets'][0]);a['id']='second';d['assets'].append(a)
  with self.assertRaises(ReportError):assess(d,NOW,max_assets=1)
 def test_calendar_invalid(self):
  with self.assertRaises(ReportError):assess(fixture(),'2026-02-30T00:00:00Z')
 def test_extra_fields(self):
  d=fixture();d['assets'][0]['token']='synthetic-unsupported'
  with self.assertRaises(ReportError):assess(d,NOW)

 def test_cli_output_collision(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);p=root/'in.json';p.write_text(json.dumps(fixture()),encoding='utf-8');out=root/'out.json';args=[sys.executable,'-m','backup_auditor',str(p),'--observed-at',NOW,'--output',str(out)]
   for code in [0,3]:
    r=subprocess.run(args,capture_output=True,text=True,timeout=20);self.assertEqual(r.returncode,code,r.stdout+r.stderr)
 def test_cli_invalid_no_echo(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'bad.json';p.write_text('{"SENSITIVE_MARKER":NaN}',encoding='utf-8');r=subprocess.run([sys.executable,'-m','backup_auditor',str(p),'--observed-at',NOW,'--output',str(Path(tmp)/'out.json')],capture_output=True,text=True,timeout=20);self.assertEqual(r.returncode,3);self.assertNotIn('SENSITIVE_MARKER',r.stdout+r.stderr)
