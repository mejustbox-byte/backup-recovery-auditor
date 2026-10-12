import argparse,json
from opsec_reports.core import load,write_new,outcome,ReportError
from .core import assess
def main():
 p=argparse.ArgumentParser(prog='backup-audit');p.add_argument('input');p.add_argument('--max-assets',type=int,default=1000);p.add_argument('--observed-at',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 try:
  r=assess(load(a.input),a.observed_at,a.max_assets);write_new(a.output,json.dumps(r,ensure_ascii=False,indent=2)+'\n');print('report_written');return outcome(r)
 except (ReportError,OSError):print('invalid_input_or_output');return 3
