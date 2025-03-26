import numpy as np 
import pandas as pd 
data = [10, 15, 20, 25, 30, 35, 40, 45, 50] 
data_series = pd.Series(data) 
mean_value_numpy = np.mean(data) 
print(f"Mean using NumPy: {mean_value_numpy}") 
mean_value_pandas = data_series.mean() 
print(f"Mean using Pandas: {mean_value_pandas}") 
descriptive_stats = data_series.describe() 
print("\nDescriptive Statistics (using Pandas):\n", descriptive_stats)
