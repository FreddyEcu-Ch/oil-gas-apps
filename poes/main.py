import numpy as np
from poes.model.poes import poes
from scipy.stats import expon, lognorm, norm, triang, uniform

# %% Define input variables
area = 25
h = 40
poro = 0.30
swi = 0.2
boi = 30

print(poes(area, h, poro, swi, boi))

# %% Defined Arrays for STOIIP
area = np.array([450.0, 500.0, 550.0])
h = np.array([30.0, 40.0, 50.0])
poro = np.array([0.12, 0.14, 0.16])
swc = np.array([0.30, 0.35, 0.40])
boi = np.array([1.01, 1.1, 1.12])

print(np.around(poes(area, h, poro, swc, boi), 2))


# %% Defining random values for porosity from norm_values variable

# Normal distribution
porosity_norm = norm.rvs(loc=0.2, scale=0.05, size=1000)
porosity_norm = np.where(porosity_norm < 0, 0, porosity_norm)
porosity_norm = np.where(porosity_norm > 0.4, 0.4, porosity_norm)
#print(porosity_norm)

# Log normal distribution
porosity_log = lognorm.rvs(s=0.8, loc=0, scale=0.2, size=1000)
porosity_log = np.where(porosity_log < 0, 0, porosity_log)
porosity_log = np.where(porosity_log > 0.4, 0.4, porosity_log)
#print(porosity_log)

# Exponential distribution
porosity_exp = expon.rvs(loc=0, scale=0.05, size=1000)
porosity_exp = np.where(porosity_exp > 0.4, 0.4, porosity_exp)
#print(porosity_exp)

# Triangular distribution
porosity_tri = triang.rvs(c=0.3, loc=0, scale=0.4, size=1000)
#print(porosity_tri)

# Uniform distribution
porosity_uni = uniform.rvs(loc=0, scale=0.4, size=1000)
#print(porosity_uni)


# %% Defining random values for area from norm_values variable

# Normal distribution
area_norm = norm.rvs(loc=190, scale=100, size=1000)
area_norm = np.where(area_norm < 50, 50, area_norm)
area_norm = np.where(area_norm > 500, 500, area_norm)
#print(area_norm)

# Log normal distribution
area_log = lognorm.rvs(s=0.8, loc=50, scale=100, size=1000)
area_log = np.where(area_log < 50, 50, area_log)
area_log = np.where(area_log > 500, 500, area_log)
#print(area_log)

# Exponential distribution
area_exp = expon.rvs(loc=50, scale=100, size=1000)
area_exp = np.where(area_exp > 500, 500, area_exp)
#print(area_exp)

# Triangular distribution
area_tri = triang.rvs(c=0.3, loc=50, scale=450, size=1000)
#print(area_tri)

# Uniform distribution
area_uni = uniform.rvs(loc=50, scale=500, size=1000)
print(area_uni)

########################################################################################################################3
#TAREA JANNER
import numpy as np
#from poes.model.poes import poes
from scipy.stats import expon, lognorm, norm, triang, uniform



# %% Defining random values for porosity from norm_values variable

# Normal distribution
thickness_norm = norm.rvs(loc=50, scale=70, size=1000)
thickness_norm = np.where(thickness_norm < 0, 0, thickness_norm)
thickness_norm = np.where(thickness_norm > 180, 180, thickness_norm)
print(thickness_norm)

# Log normal distribution
thickness_log = lognorm.rvs(s=0.6, loc=0, scale=40, size=1000)
thickness_log = np.where(thickness_log < 0, 0, thickness_log)
thickness_log = np.where(thickness_log > 180, 180, thickness_log)
print(thickness_log)

# Exponential distribution
thickness_exp = expon.rvs(loc=0, scale=50, size=1000)
thickness_exp = np.where(thickness_exp > 180, 180, thickness_exp)
print(thickness_exp)
#
# Triangular distribution
thickness_tri = triang.rvs(c=0.3, loc=0, scale=150, size=1000)
print(thickness_tri)

# Uniform distribution
thickness_uni = uniform.rvs(loc=0, scale=200, size=1000)
print(thickness_uni)
#End of homework