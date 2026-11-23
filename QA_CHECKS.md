# Quality assurance checklist

## Source-file checks recorded in the workbook

| Check | Recorded result |
|---|---:|
| Population rows | 19,747 |
| Distinct economy codes | 217 |
| Year coverage | 1960–2050 |
| Country grouping rows | 218 |
| Unmatched population economy codes | 0 |
| Duplicate economy-year records | 0 |
| Missing female population | 138 |
| Missing urban population | 293 |
| Missing rural population | 293 |
| Missing annual population growth | 6,108 |

The workbook records 19,454 comparable records for the urban/rural reconciliation check. Urban plus rural population reconciles to derived total population within two people across those comparable records.

## Workbook structure checks

The QA script verifies:
- Required worksheet names.
- Source Data row and column counts.
- Minimum and maximum year.
- Distinct economy-code count.
- Dashboard chart counts.
- Data-validation rules on both dashboard sheets.
- The presence of expected selector cells.

## Manual Excel checks

Before public release, open the workbook in Microsoft Excel desktop and verify:
- [ ] Click **Enable Editing** if Protected View appears.
- [ ] Dashboard 1 Year selector opens and changes the KPI cards.
- [ ] Dashboard 1 Region selector opens and filters the selected slice.
- [ ] Dashboard 1 Income Group selector opens and filters the selected slice.
- [ ] Dashboard 2 Region and Income Group selectors work.
- [ ] Charts remain visible and update as expected.
- [ ] The analytical report and methodology sheets remain readable.
- [ ] Save the manually tested workbook and reopen it once before publishing.

## Limits of automated validation

The Python QA script checks workbook structure and validation definitions. It cannot fully emulate Microsoft Excel's calculation engine or prove that dropdown interactions work in the user's installed Excel application. Manual testing is required.
