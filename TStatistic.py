import numpy as np 
from scipy import stats 
group1 = np.array([25, 30, 35, 40, 45, 50, 55]) 
group2 = np.array([30, 35, 40, 45, 50, 55, 60]) 
t_stat, p_value = stats.ttest_ind(group1, group2) 
print(f"T-Statistic: {t_stat}") 
print(f"P-value: {p_value}") 
alpha = 0.05 
if p_value < alpha: 
    print("Reject the null hypothesis (H0): The means are significantly different.") 
else: 
    print("Fail to reject the null hypothesis (H0): The means are not significantly different.") 
