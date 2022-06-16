import numpy as np

from scipy.stats import expon, lognorm, norm, triang, uniform


# Normal distribution
SWI_norm = norm.rvs(loc=1.5, scale=0.5, size=1000)
SWI_norm = np.where(SWI_norm < 1, 1, SWI_norm)
SWI_norm = np.where(SWI_norm > 2, 2, SWI_norm)
print(SWI_norm)

# Log normal distribution
SWI_log = lognorm.rvs(s=0.7, loc=1, scale=0.2, size=1000)
SWI_log = np.where(SWI_log < 1, 1, SWI_log)
SWI_log = np.where(SWI_log > 2, 2, SWI_log)
print(SWI_log)

# Exponential distribution
SWI_exp = expon.rvs(loc=1, scale=0.2, size=1000)
SWI_exp = np.where(SWI_exp > 2, 2, SWI_exp)
print(SWI_exp)

# Triangular distribution
SWI_tri = triang.rvs(c=0.3, loc=1, scale=1, size=1000)
print(SWI_tri)

# Uniform distribution
SWI_uni = uniform.rvs(loc=1, scale=1, size=1000)
print(SWI_uni)