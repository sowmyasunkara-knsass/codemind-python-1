import numpy as np 
from scipy.stats import skew 
data = [10, 12, 23, 23, 16, 23, 21, 16, 23, 25, 30] 
skewness = skew(data) 
print(f"Sample Data: {data}") 
print(f"Skewness: {skewness}")
