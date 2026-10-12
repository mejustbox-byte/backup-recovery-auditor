# Check matrix

| ID | Pass | Fail | Unknown |
|---|---|---|---|
| BAK-001 | Both excessive permission flags false | Either true | Null without a known failure |
| BAK-002 | Encryption and separate key access true | Either false | Null without a known failure |
| BAK-003 | Immutable and verified true | Either false | Null without a known failure |
| BAK-004 | Successful dated test within age limit | Failure or stale success | Missing timestamp or unknown result |

BAK-004 fail severity is critical; other failures are high. Non-fail severities are info. A success at exactly the maximum age passes; one second older fails. An explicit failure remains fail even without a timestamp. Future timestamps reject the input rather than manufacturing freshness. Immutability_verified is a supplied assertion, not independent policy inspection.

[Index](index.md) · [Other language](../ru/check-matrix.md)
