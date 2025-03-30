import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
data = [12, 7, 9, 15, 19, 3, 8, 14, 10, 6] 
data_series = pd.Series(data) 
Q1 = np.percentile(data, 25) 
Q3 = np.percentile(data, 75) 
IQR = Q3 - Q1 
lower_bound = Q1 - 1.5 * IQR 
upper_bound = Q3 + 1.5 * IQR
print(f"1st Quartile (Q1): {Q1}") 
print(f"3rd Quartile (Q3): {Q3}") 
print(f"Interquartile Range (IQR): {IQR}") 
print(f"Lower Bound for Outliers: {lower_bound}") 
print(f"Upper Bound for Outliers: {upper_bound}") 
plt.figure(figsize=(8, 6)) 
sns.boxplot(data=data_series, color="lightblue", width=0.5) 
plt.title("Box Plot with IQR Visualization") 
plt.show() 
