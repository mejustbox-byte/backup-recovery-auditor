from datetime import datetime, timezone
from opsec_reports.core import ReportError, make_report
from opsec_reports.adapters import result
VERSION='0.1.0a1'
def require(ok):
 if not ok:raise ReportError('invalid_backup_input')
def keys(obj,names):require(isinstance(obj,dict) and set(obj)==set(names))
def date(value):
 require(isinstance(value,str) and len(value)==20 and value.endswith('Z'))
 try:
  parsed=datetime.strptime(value,'%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
  require(parsed.strftime('%Y-%m-%dT%H:%M:%SZ')==value)
  return parsed
 except ValueError:raise ReportError('invalid_date') from None
def assess(data,now,max_assets=1000):
 require(type(max_assets) is int and 1<=max_assets<=1000)
 keys(data,['schema_version','scope','synthetic','assets']);require(data['schema_version']=='backup-1.0');require(isinstance(data['scope'],str) and 0<len(data['scope'])<=128);require(type(data['synthetic']) is bool);require(isinstance(data['assets'],list) and 0<len(data['assets'])<=max_assets)
 at=date(now);records=[];seen=set()
 for a in data['assets']:
  keys(a,['id','excessive_read','excessive_delete','encrypted','key_access_separate','immutable','immutability_verified','restore'])
  require(isinstance(a['id'],str) and 0<len(a['id'])<=128 and a['id'] not in seen);seen.add(a['id'])
  for k in ['excessive_read','excessive_delete','encrypted','key_access_separate','immutable','immutability_verified']:require(a[k] is None or type(a[k]) is bool)
  statuses=[]
  for fields,bad in [(['excessive_read','excessive_delete'],True),(['encrypted','key_access_separate'],False),(['immutable','immutability_verified'],False)]:
   vals=[a[k] for k in fields];statuses.append('fail' if any(v is bad for v in vals) else 'not_tested' if any(v is None for v in vals) else 'pass')
  restore=a['restore'];keys(restore,['tested_at','result','maximum_age_days']);require(type(restore['maximum_age_days']) is int and 1<=restore['maximum_age_days']<=3650);require(restore['result'] in ['success','failure','unknown']);require(restore['tested_at'] is None or isinstance(restore['tested_at'],str))
  tested=None if restore['tested_at'] is None else date(restore['tested_at'])
  require(tested is None or tested<=at)
  status='fail' if restore['result']=='failure' else 'not_tested' if tested is None or restore['result']=='unknown' else 'fail' if (at-tested).total_seconds()>restore['maximum_age_days']*86400 else 'pass'
  statuses.append(status)
  for i,status in enumerate(statuses,1):
   r=result(f'BAK-00{i}',a['id'],status,('critical' if i==4 else 'high') if status=='fail' else 'info');r['message']='Backup declaration '+status;records.append(r)
 return make_report('backup-recovery-auditor',VERSION,'backup-1.0',data['scope'],now,data['synthetic'],records)
