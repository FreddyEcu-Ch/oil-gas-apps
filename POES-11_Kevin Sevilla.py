import numpy as np
from poes.model.poes import poes
from scipy.stats import expon, lognorm, norm, triang, uniform

# %% Define input variables
area = 25
h = 40
poro = 0.30
swi = 0.2
boi = 30

#print(poes(area, h, poro, swi, boi))

# %% Defined Arrays for STOIIP
area = np.array([450.0, 500.0, 550.0])
h = np.array([30.0, 40.0, 50.0])
poro = np.array([0.12, 0.14, 0.16])
swc = np.array([0.30, 0.35, 0.40])
boi = np.array([1.01, 1.1, 1.12])

#print(np.around(poes(area, h, poro, swc, boi), 2))

# %% Defining random values for porosity from norm_values variable

# Normal distribution
BOi_norm = norm.rvs(loc=1.5, scale=0.5, size=1000)
BOi_norm = np.where(BOi_norm < 1, 1, BOi_norm)
BOi_norm = np.where(BOi_norm > 2, 2, BOi_norm)
#print(BOi_norm)

# Log normal distribution
BOi_log = lognorm.rvs(s=0.7, loc=1, scale=0.2, size=1000)
BOi_log = np.where(BOi_log < 1, 1, BOi_log)
BOi_log = np.where(BOi_log > 2, 2, BOi_log)
#print(BOi_log)

# Exponential distribution
BOi_exp = expon.rvs(loc=1, scale=0.2, size=1000)
BOi_exp = np.where(BOi_exp > 2, 2, BOi_exp)
#print(BOi_exp)

# Triangular distribution
BOi_tri = triang.rvs(c=0.3, loc=1, scale=1, size=1000)
#print(BOi_tri)

# Uniform distribution
BOi_uni = uniform.rvs(loc=1, scale=1, size=1000)
print(BOi_uni)

