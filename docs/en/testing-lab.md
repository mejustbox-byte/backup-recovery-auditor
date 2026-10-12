# Verification and real restore evidence

Unit tests cover every implemented control, unknown values, strict types, restore failure/staleness, exact time boundaries, invalid calendars, duplicate IDs, unknown fields and asset budgets. CLI checks separately cover exit codes and output collisions. Public inputs are synthetic.

Actual restore testing belongs in an isolated environment with private execution records. Record the exact backup, environment, operator, key availability, start/end time and integrity checks outside this neutral public fixture. Only after review should a normalized declaration be exported. No actual restore or production storage connection was exercised for this candidate.

[Index](index.md) · [Other language](../ru/testing-lab.md)
