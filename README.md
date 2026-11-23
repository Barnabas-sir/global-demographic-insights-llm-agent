# Global Demographic Insights
## Interactive Excel Dashboard & LLM-Assisted Analytics Workflow

An end-to-end demographic analytics portfolio project exploring population change and urbanisation across 217 economies from 1960 to 2050. The deliverable combines an interactive Microsoft Excel dashboard, a written analytical report, data-quality documentation, original source files and an auditable LLM-assisted workflow.

> **Project type:** LLM-assisted analytics capstone  
> **Primary deliverable:** Interactive Excel workbook  
> **Analysis period:** 1960–2050  
> **Geographic coverage:** 217 economies  
> **Workbook:** [`workbook/Global_Demographic_Insights_Interactive_Dashboard.xlsx`](workbook/Global_Demographic_Insights_Interactive_Dashboard.xlsx)

## Project overview

The project examines how population size and settlement patterns evolve over time. It focuses on total, urban and rural population and compares demographic patterns across geographic regions and income groups.

### Questions explored
- How does the combined population of the economies represented in the dataset change from 1960 to 2050?
- How do urban and rural population trajectories differ?
- How does the urban share evolve over time?
- How do demographic patterns vary by region and income group?
- Which regions and economies show the strongest projected urban population growth?

## Dashboard preview

![Global demographic dashboard in Excel](screenshots/dashboard_global_interactive.png)

## Workbook features

The workbook contains ten worksheets:

| Worksheet | Purpose |
|---|---|
| Dashboard 1 – Global | Global population KPIs, annual trend charts and filter controls |
| Dashboard 2 – Regions | Regional and country-level comparisons |
| Analytical Report | Executive summary, findings and interpretation |
| Methodology & Data Quality | Definitions, transformation logic, checks and limitations |
| Work Log | Chronological record of the analytical workflow |
| Source Data | Population records and derived fields |
| Country Groups | Economy, region and income-group lookup |
| Indicator Metadata | Indicator definitions and aggregation guidance |
| _Chart Data | Supporting chart calculations |
| Lists | Dropdown selector values |

### Interactive controls

**Dashboard 1 – Global:** Year, Region and Income Group selectors.  
**Dashboard 2 – Regions:** Region and Income Group selectors.

The dropdowns use Excel Data Validation. Open the workbook in Microsoft Excel desktop, enable editing if prompted, select a yellow filter cell and use its dropdown arrow or `Alt` + `Down Arrow`.

## Key findings recorded in the workbook

| Measure | 2023 | 2050 |
|---|---:|---:|
| Total population | 8.00 billion | 9.65 billion |
| Urban population | 4.58 billion | 6.55 billion |
| Rural population | 3.42 billion | 3.09 billion |
| Urban share | 57.3% | 67.9% |

These totals are sums across the economies represented in the supplied file. They should not be described as official World Bank global aggregates unless independently reconciled to an official aggregate series.

## Raw source data included

The original files are preserved under [`data/raw/`](data/raw/):

1. `Population_Figures_and_Projections.csv` — primary demographic observations and projections.
2. `Country_Groupings.xlsx` — country/economy, region and income-group lookup.
3. `Population_Figures_and_Projections_Metadata.xlsx` — indicator definitions and source notes.

The same inputs are integrated into the workbook's `Source Data`, `Country Groups` and `Indicator Metadata` worksheets. The raw files are included separately so reviewers can inspect the original inputs and compare them with the workbook.

## Methodology and LLM-agent workflow

The workflow covers task interpretation, source inventory, schema review, transformation planning, aggregation, dashboard construction, insight generation, quality assurance and documentation. The LLM is treated as an analytics copilot with explicit human checkpoints; this repository does not claim a deployed autonomous agent.

- [`docs/AGENT_DESIGN.md`](docs/AGENT_DESIGN.md) — agent stages, tool boundaries, human approvals and guardrails.
- [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) — joins, derived measures and aggregation logic.
- [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md) — source field definitions.
- [`docs/QA_CHECKS.md`](docs/QA_CHECKS.md) — automated and manual validation checklist.
- [`docs/WORK_LOG.md`](docs/WORK_LOG.md) — project activity record.

## Reproduce and inspect

Microsoft Excel desktop is recommended for interactive use. To run the optional structural QA script:

```bash
python -m pip install -r requirements.txt
python scripts/validate_workbook.py workbook/Global_Demographic_Insights_Interactive_Dashboard.xlsx
```

The script checks workbook structure, expected worksheets, source-data dimensions, year coverage, charts and selector validation rules. It does not emulate Excel's calculation engine; manual interaction testing is still required.

## Data attribution and licensing

The supplied metadata identifies the World Bank and upstream providers including the United Nations Population Division, national statistical offices and Eurostat. Terms can differ by indicator and provider. **Before making this repository public, review the applicable terms and confirm that redistribution of the raw source files is permitted.** The project-authored documentation/script license does not relicense third-party data.

Official references:
- [World Bank data licensing](https://datacatalog.worldbank.org/public-licenses)
- [World Bank data terms of use](https://data.worldbank.org/summary-terms-of-use)
- [UN World Population Prospects](https://population.un.org/wpp/)
- [UN World Urbanization Prospects](https://population.un.org/wup/)

This project is independent and is not endorsed by the World Bank or the United Nations.

## Repository structure

```text
global-demographic-insights-llm-agent/
├── README.md
├── CHANGELOG.md
├── LICENSE.md
├── requirements.txt
├── .gitignore
├── workbook/
│   └── Global_Demographic_Insights_Interactive_Dashboard.xlsx
├── screenshots/
│   └── dashboard_global_interactive.png
├── data/
│   ├── README.md
│   └── raw/
│       ├── Population_Figures_and_Projections.csv
│       ├── Country_Groupings.xlsx
│       └── Population_Figures_and_Projections_Metadata.xlsx
├── docs/
│   ├── AGENT_DESIGN.md
│   ├── DATA_DICTIONARY.md
│   ├── METHODOLOGY.md
│   ├── QA_CHECKS.md
│   └── WORK_LOG.md
└── scripts/
    └── validate_workbook.py
```

## Future enhancements

- Build a reproducible end-to-end Python transformation pipeline.
- Add automated regression tests for key calculations.
- Add a controlled refresh process for newer source releases.
- Extend regional analysis with defensible weighted rates.
- Add source-to-output lineage for every KPI and chart.
