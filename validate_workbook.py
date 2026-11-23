#!/usr/bin/env python3
"""Structural QA checks for the Global Demographic Insights Excel workbook.

This script validates workbook structure and selector definitions. It does not
recalculate Excel formulas or emulate Microsoft Excel's interactive UI.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

import openpyxl


EXPECTED_SHEETS = [
    "Dashboard 1 - Global",
    "Dashboard 2 - Regions",
    "Analytical Report",
    "Methodology & Data Quality",
    "Work Log",
    "Source Data",
    "Country Groups",
    "Indicator Metadata",
    "_Chart Data",
    "Lists",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("workbook", type=Path, help="Path to the .xlsx workbook")
    args = parser.parse_args()

    if not args.workbook.exists():
        print(f"ERROR: File not found: {args.workbook}")
        return 2

    wb = openpyxl.load_workbook(args.workbook, data_only=False)
    errors: list[str] = []
    warnings: list[str] = []

    missing = [name for name in EXPECTED_SHEETS if name not in wb.sheetnames]
    if missing:
        errors.append(f"Missing worksheets: {missing}")

    if "Source Data" in wb.sheetnames:
        ws = wb["Source Data"]
        expected_rows = 19748  # header + 19,747 source records
        if ws.max_row != expected_rows:
            errors.append(f"Source Data row count is {ws.max_row}; expected {expected_rows}.")
        if ws.max_column < 12:
            errors.append(f"Source Data has {ws.max_column} columns; expected at least 12.")
        years = [ws.cell(row, 3).value for row in range(2, ws.max_row + 1)
                 if isinstance(ws.cell(row, 3).value, (int, float))]
        if years and (min(years) != 1960 or max(years) != 2050):
            errors.append(f"Unexpected year range: {min(years)}–{max(years)}.")

        codes = [ws.cell(row, 2).value for row in range(2, ws.max_row + 1)
                 if ws.cell(row, 2).value]
        if len(set(codes)) != 217:
            warnings.append(f"Distinct country-code count is {len(set(codes))}; expected 217.")

    expected_validations = {
        "Dashboard 1 - Global": {"B3", "E3", "H3"},
        "Dashboard 2 - Regions": {"B3", "E3"},
    }
    for sheet, expected_cells in expected_validations.items():
        if sheet not in wb.sheetnames:
            continue
        ws = wb[sheet]
        actual_cells: set[str] = set()
        for validation in ws.data_validations.dataValidation:
            for cell_range in validation.sqref.ranges:
                # This project uses single-cell selector ranges.
                actual_cells.add(str(cell_range))
        missing_cells = expected_cells - actual_cells
        if missing_cells:
            errors.append(f"{sheet} missing data-validation cells: {sorted(missing_cells)}")

    for sheet in ["Dashboard 1 - Global", "Dashboard 2 - Regions"]:
        if sheet in wb.sheetnames and len(wb[sheet]._charts) == 0:
            errors.append(f"{sheet} has no charts.")

    print(f"Workbook: {args.workbook}")
    print(f"Worksheets found: {len(wb.sheetnames)}")
    for sheet in ["Dashboard 1 - Global", "Dashboard 2 - Regions"]:
        if sheet in wb.sheetnames:
            ws = wb[sheet]
            print(
                f"{sheet}: {len(ws._charts)} chart(s), "
                f"{len(ws.data_validations.dataValidation)} validation rule(s)"
            )

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1

    print(f"PASSED: structural checks complete ({len(warnings)} warning(s)).")
    print("Manual Excel interaction testing is still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
