import pandas as pd 
data = [12, 7, 9, 15, 19, 3, 8, 14, 10, 6] 
data_series = pd.Series(data)  
percentiles = [25, 50, 75, 90] 
percentile_values = data_series.quantile([p / 100 for p in percentiles]) 
for percentile, value in zip(percentiles, percentile_values): 
    print(f"{percentile}th percentile: {value}")
