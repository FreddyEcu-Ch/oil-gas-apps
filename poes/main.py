import numpy as np
from poes.model.poes import poes

# %% Define input variables
area = 25
h = 40
poro = 0.30
swi = 0.2
boi = 30

print(poes(area,h,poro,swi,boi))

# %% Defined Arrays for STOIIP
area = np.array([450.0, 500.0, 550.0])
h = np.array([30.0, 40.0, 50.0])
poro = np.array([0.12, 0.14, 0.16])
swc = np.array([0.30, 0.35, 0.40])
boi = np.array([1.01, 1.1, 1.12])

print(np.around(poes(area, h, poro, swc, boi), 2))


