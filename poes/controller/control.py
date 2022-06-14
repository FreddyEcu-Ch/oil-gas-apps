import xlwings as xw
import numpy as np
import pandas as pd
from poes.model.poes import poes

# Crete names for sheets
SHEET_SUMMARY = "Resumen"
SHEET_RESULTS = "Resultados"

# Call cells
DET_VALUES = "det_values"

# Call poes cell
DET_POES = "poes"


def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[SHEET_SUMMARY]

    # Calculate Deterministic POES
    params = sheet[DET_VALUES].options(np.array, transpose=True).value
    sheet[DET_POES].value = poes(*params)


if __name__ == "__main__":
    xw.Book("control.xlsm").set_mock_caller()
    main()
