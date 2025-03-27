import numpy as np
import pandas as pd
from scipy import stats
data = [10, 15, 20, 20, 25, 30, 35, 40, 45, 50, 20]
data_series = pd.Series(data)
mode_value_pandas = data_series.mode()
print(f"Mode using Pandas: {mode_value_pandas[0]}")
mode_value_scipy = stats.mode(data)
print(f"Mode using SciPy: {mode_value_scipy.mode} (Frequency: {mode_value_scipy.count})")
descriptive_stats = data_series.describe()
print("\nDescriptive Statistics (using Pandas):\n", descriptive_stats)
