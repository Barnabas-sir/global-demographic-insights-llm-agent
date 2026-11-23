# Methodology

## Scope

The workbook analyses the supplied annual population dataset for 217 economies from 1960 through 2050. The dataset contains 19,747 economy-year rows and 12 source columns.

## Source integration

The population file is joined to the country-grouping reference using the economy/country code:
- Population key: `Country Code`
- Lookup key: `Code`
- Attributes added: `Region`, `Income group`

The source review recorded no unmatched population-file codes. The grouping reference contains one more economy than the population file.

## Derived measures

### Total population

At economy-year level:

`Total population = Female population + Male population`

The derived total is null when the necessary source components are unavailable.

### Urban share

At economy-year level:

`Urban share = Urban population / (Urban population + Rural population)`

The calculation is only meaningful when both urban and rural values are available and the denominator is non-zero.

### Aggregation

- Population counts are additive and are summed across included economies.
- Percentages and rates are not summed.
- Regional rates require a defensible weighting denominator; a simple arithmetic mean should not be presented as a population-weighted regional rate.
- The workbook's regional and global-style sums reflect the supplied economy coverage. They are not automatically equivalent to official World Bank regional/global aggregate series.

## Interpretation

Historical estimates and future projections should be distinguished. Values beyond the historical observation period are projections and should be interpreted as scenario-dependent estimates, not certainties.

Urban/rural classifications vary by national statistical office. The supplied metadata also notes that aggregation of urban and rural population may not equal total population because of country-coverage differences.

## Reconciliation

The workbook's methodology worksheet records 19,454 comparable records for the urban/rural reconciliation check. In those records, urban plus rural population reconciles to the derived total population within two people. This is a check on the supplied records, not a universal property of the indicators.

## Known missingness

The supplied source contains missing values in several indicators. In particular, the population-growth annual percentage series has 6,108 missing values out of 19,747 records (approximately 30.9%). Missing values are not silently filled.

See the workbook's `Methodology & Data Quality` sheet for the full source inventory and detailed quality checks.
