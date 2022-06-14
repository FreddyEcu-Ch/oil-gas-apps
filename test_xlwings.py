#%% Pregunta 8 - Lección
import pandas as pd
import xlwings as xw
import numpy as np

# Generar un workbook de MS Excel
xb = xw.Book()
sheet = xb.sheets["sheet1"]

#%% Create a numpy array
rango = "B1:B5"
sheet[rango].options(np.array, transpose=True).value = np.array([1, 2, 3, 4, 5])

#%% Create a Dataframe
sheet["E5"].options(pd.DataFrame, index=False, expand="table").value = pd.DataFrame(
    {"Variables": ["poro", "sw", "h"], "Valores": [0.20, 0.51, 40]}
)

#%% Call a dataframe from MS Excel
df = sheet["C11"].options(pd.DataFrame, index=False, expand='table').value

#%%
print(df)