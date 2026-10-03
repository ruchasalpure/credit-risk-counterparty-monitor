# Duties and Responsibilities for Credit Risk Counterparty Monitor Agent

## Dual-Control Architecture
Maker:
pfe-calculator

Checker:
collateral-adequacy-checker

## Operational Workflow
1. The Maker (pfe-calculator) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (collateral-adequacy-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
