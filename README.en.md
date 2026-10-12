# Backup & Recovery Auditor

Install the bootstrap dependency before this package. Use explicit UTC observation time for reproducible restore age. Output paths must not exist. Exit codes: 0 all declared checks pass, 1 known failure, 2 incomplete evidence without failures, 3 invalid input/output. Unknown evidence is retained in coverage gaps. The normalized result is directly consumable by the report-contract CLI.

```bash
python -m pip install -r requirements-bootstrap.txt
python -m pip install .
backup-audit examples/safe.synthetic.json --observed-at 2026-10-12T00:00:00Z --output report.json
opsec-report validate report.json
opsec-report html report.json --output report.html
```

[Documentation](docs/en/index.md)

Local candidate 0.1.0a1; hosted CI and release pending. No actual restore performed.
