# Input backup-1.0

The root contains exactly schema_version, scope, synthetic and assets. Scope is a nonempty string up to 128 characters; synthetic is a strict boolean. Assets is nonempty and contains unique IDs up to 128 characters. The bundled safe.synthetic.json is the complete input example.

Each asset declares excessive_read, excessive_delete, encrypted, key_access_separate, immutable and immutability_verified as true, false or null. Null means unknown. These are neutral declarations; no vendor ACL or retention-policy parser is implemented. The restore object contains exactly tested_at, result and maximum_age_days. Result is success/failure/unknown; timestamp is UTC YYYY-MM-DDTHH:MM:SSZ or null; maximum_age_days is an integer from 1 to 3650.

[Index](index.md) · [Other language](../ru/input-format.md)
