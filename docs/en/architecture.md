# Architecture

CLI → bounded strict JSON loader → exact-field model → pure checks → normalized report → exclusive new output. The released opsec-report-contract 0.1.0a1 supplies parsing, coverage and output validation. No source messages or storage credentials are accepted.

Inputs are bounded to 8 MiB and depth 64 by the contract loader. The asset limit defaults to 1000 and can be lowered with --max-assets. Each asset produces four records with unique check/asset identity. Unknown records make coverage incomplete. Generic messages avoid echoing source material, but scope and asset IDs remain sensitive user declarations.

[Index](index.md) · [Other language](../ru/architecture.md)
