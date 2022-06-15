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

# Triangular distribution
thickness_tri = triang.rvs(c=0.3, loc=0, scale=150, size=1000)
print(thickness_tri)

# Uniform distribution
thickness_uni = uniform.rvs(loc=0, scale=200, size=1000)
print(thickness_uni)
#End of homework