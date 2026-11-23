# LLM-assisted agent workflow design

## Purpose

Define a bounded, auditable workflow for using an LLM as an analytics copilot on a demographic dashboard task. The workflow supports planning, source interpretation, quality review and documentation. It does not represent a deployed autonomous agent or a self-running data product.

## Agent role

**Role:** Demographic Analytics Copilot

**Objective:** Help transform supplied demographic files into a traceable Excel dashboard and analytical report while preserving source meaning and surfacing uncertainty.

## Inputs

- Population Figures & Projections CSV.
- Country Groupings workbook.
- Population Figures & Projections Metadata workbook.
- Dashboard design reference supplied by the project owner.
- User requirements for at least two dashboard pages, an analytical report and an audit trail.

## Workflow stages

| Stage | LLM/agent responsibility | Required evidence/output | Human checkpoint |
|---|---|---|---|
| 1. Task framing | Convert request into deliverables and acceptance criteria | Scope and output checklist | Confirm scope |
| 2. Source inventory | Identify each input, schema and intended use | Source inventory | Confirm source files |
| 3. Schema review | Identify keys, years, measures, missingness and metadata | Schema and data-quality profile | Resolve ambiguous fields |
| 4. Transformation planning | Propose joins and derived measures | Transformation specification | Approve formulas |
| 5. Calculation | Assist with formulas and aggregation logic | Calculated fields and reconciliation checks | Review calculations |
| 6. Visualisation | Plan dashboard layout, filters and charts | Two dashboard pages | Test interactions in Excel |
| 7. Interpretation | Draft findings tied to calculated outputs | Analytical report | Verify every numeric claim |
| 8. QA | Check coverage, formulas, validations, charts and limitations | QA checklist and work log | Approve release |
| 9. Publication preparation | Create README, methodology and reproducibility notes | GitHub-ready project structure | Review attribution and public files |

## Tool boundaries

- **Excel:** final interactive workbook, formulas, data validation, charts and report worksheets.
- **Python/pandas:** optional structural and data-quality checks.
- **openpyxl:** workbook inspection and validation-rule/chart inventory.
- **LLM:** task decomposition, transformation reasoning, documentation drafting and QA assistance.
- **Human operator:** final decision-maker for source selection, interpretation, Excel interaction testing and publication.

## Guardrails

1. Never overwrite or silently modify raw source values.
2. Do not impute missing population values unless an explicit method is approved and documented.
3. Distinguish observed historical values from projected values.
4. Sum additive population counts; do not sum rates or percentages.
5. Use weighted aggregation for rates only when a defensible denominator/weight is available and the indicator metadata supports it.
6. Do not label economy-level sums as official global aggregates without reconciliation to an official aggregate series.
7. Keep source-derived facts separate from model-generated interpretation.
8. Cite source providers and retain indicator metadata.
9. Do not claim the World Bank or UN endorses the project.
10. Require a human test of dropdowns, KPI changes and charts in desktop Excel before publishing.

## Failure handling

- **Unmatched economy codes:** stop the affected aggregation, report the unmatched codes and request a mapping decision.
- **Missing values:** retain nulls, quantify missingness and disclose the impact.
- **Unexpected duplicate keys:** inspect economy-year duplicates before aggregating.
- **Broken Excel validation:** inspect the cell-level validation rule and source range; test in desktop Excel after enabling editing.
- **Excel repair prompt:** retain an untouched backup, open/repair a copy, test the repaired copy and publish only the copy that has been manually verified.
- **Contradictory totals:** reconcile source coverage and aggregation logic before changing reported results.

## Acceptance criteria

- Workbook has two dashboard pages and a report/methodology section.
- Filter controls are usable in desktop Excel.
- Every KPI has a defined calculation.
- Key totals reconcile to the documented aggregation logic.
- Known missingness and coverage limitations are disclosed.
- Work log records major transformations and QA actions.
- Public repository includes attribution and does not imply institutional endorsement.
