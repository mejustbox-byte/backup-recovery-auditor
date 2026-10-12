# Threat model

Untrusted input may contain malformed JSON, misleading settings or private identifiers. Strict types, exact fields, byte/depth limits, duplicate rejection and exclusive output reduce common input hazards. No network collector or input execution exists. Invalid input produces generic errors without source values.

Residual risks include dishonest declarations, filesystem races, hardlinks, runtime/dependency bugs and CPU/RAM use within bounded input. Asset IDs and scope are not anonymized. The auditor does not authenticate a restore record, verify key availability, sanitize privacy or authorize publication. Pass is only consistency with the declared policy, not recoverability proof.

[Index](index.md) · [Other language](../ru/threat-model.md)
