import numpy as np 
data = [12, 7, 9, 15, 19, 3, 8, 14, 10, 6] 
percentiles = [25, 50, 75, 90] 
percentile_values = np.percentile(data, percentiles) 
for percentile, value in zip(percentiles, percentile_values): 
    print(f"{percentile}th percentile: {value}")
