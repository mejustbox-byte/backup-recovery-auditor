# Scope and acceptance

Assess declared backup protection and restore-test evidence in a neutral backup-1.0 export. The alpha supplies four checks and an opsec-1.0 report. It never connects to storage, deletes backups, fetches keys or runs restoration.

Acceptance requires positive, negative, unknown and invalid-input cases for all four checks. An absent declaration never establishes a pass; a known bad setting still fails when its companion is unknown. Unsupported fields and formats are rejected. Claims remain assertions supplied by the operator.

[Index](index.md) · [Other language](../ru/requirements.md)
