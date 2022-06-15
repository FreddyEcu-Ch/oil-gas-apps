# %% Defining random values for area from norm_values variable
import numpy as np
from scipy.stats import expon, lognorm, norm, triang, uniform

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
area_tri = triang.rvs(c=0.3, loc=50, scale=500, size=1000)
#print(area_tri)

# Uniform distribution
area_uni = uniform.rvs(loc=50, scale=500, size=1000)
print(area_uni)