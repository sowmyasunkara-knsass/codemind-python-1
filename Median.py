import numpy as np 
import pandas as pd 
data = [10, 15, 20, 25, 30, 35, 40, 45, 50] 
data_series = pd.Series(data) 
median_value_numpy = np.median(data) 
print(f"Median using NumPy: {median_value_numpy}") 
median_value_pandas = data_series.median() 
print(f"Median using Pandas: {median_value_pandas}") 
descriptive_stats = data_series.describe() 
print("\nDescriptive Statistics (using Pandas):\n", descriptive_stats)
