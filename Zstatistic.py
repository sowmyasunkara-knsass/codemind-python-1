import numpy as np 
from statsmodels.stats.weightstats import ztest 
data = np.array([23, 21, 18, 25, 30, 20, 19, 22, 21, 19]) 
z_stat, p_value = ztest(data, value=20) 
print(f"Z-Statistic: {z_stat}") 
print(f"P-value: {p_value}") 
alpha = 0.05 
if p_value < alpha: 
    print("Reject the null hypothesis (H0)") 
else: 
    print("Fail to reject the null hypothesis (H0)")
