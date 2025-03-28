import numpy as np 
import pandas as pd 
from scipy.stats import kurtosis, skew 
import matplotlib.pyplot as plt  
data = [12, 15, 23, 7, 9, 12, 13, 17, 19, 25, 30, 35, 40, 50, 60] 
data_series = pd.Series(data)  
mean = np.mean(data_series) 
median = np.median(data_series) 
mode = data_series.mode()[0] 
range_value = np.ptp(data_series) 
variance = np.var(data_series) 
std_deviation = np.std(data_series)
kurt = kurtosis(data_series)  
skewness = skew(data_series)  
print(f"Sample Data: {data}") 
print(f"Mean: {mean}") 
print(f"Median: {median}") 
print(f"Mode: {mode}") 
print(f"Range: {range_value}") 
print(f"Variance: {variance}") 
print(f"Standard Deviation: {std_deviation}") 
print(f"Kurtosis: {kurt}") 
print(f"Skewness: {skewness}") 
plt.figure(figsize=(10, 6)) 
plt.hist(data_series, bins=10, edgecolor='black', alpha=0.7) 
plt.axvline(mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean}') 
plt.axvline(median, color='blue', linestyle='dashed', linewidth=2, label=f'Median: {median}') 
plt.title("Histogram of the Sample Data") 
plt.xlabel("Value") 
plt.ylabel("Frequency") 
plt.legend() 
plt.show() 
