# Data dictionary

The source population file has 12 columns. Field names below are preserved from the supplied CSV.

| Field | Meaning | Unit / type | Notes |
|---|---|---|---|
| `Country Name` | Economy name | Text | Source label |
| `Country Code` | Economy identifier | Text | Join key to country-grouping lookup |
| `Time` | Calendar year | Integer | 1960–2050 |
| `Time Code` | Year code | Text | Source year identifier |
| `Population, female [SP.POP.TOTL.FE.IN]` | Female population | Persons | Additive count |
| `Population, male [SP.POP.TOTL.MA.IN]` | Male population | Persons | Additive count |
| `Population growth (annual %) [SP.POP.GROW]` | Annual population growth | Percent | Rate; do not sum |
| `Rural population [SP.RUR.TOTL]` | Rural population | Persons | Additive count; national definitions vary |
| `Urban population [SP.URB.TOTL]` | Urban population | Persons | Additive count; national definitions vary |
| `Life expectancy at birth, total (years) [SP.DYN.LE00.IN]` | Life expectancy at birth | Years | Rate/summary measure; do not sum |
| `Birth rate, crude (per 1,000 people) [SP.DYN.CBRT.IN]` | Crude birth rate | Per 1,000 people | Rate; requires weighted aggregation |
| `Death rate, crude (per 1,000 people) [SP.DYN.CDRT.IN]` | Crude death rate | Per 1,000 people | Rate; requires weighted aggregation |

## Lookup fields

| Field | Meaning |
|---|---|
| `Code` | Economy code |
| `Economy` | Economy display name |
| `Region` | World Bank region classification in the supplied lookup |
| `Income group` | Income-group classification in the supplied lookup |

## Derived workbook fields

The workbook also includes calculated total population and urban-share fields. Their formulas and use are described in `METHODOLOGY.md` and the workbook's methodology worksheet.
