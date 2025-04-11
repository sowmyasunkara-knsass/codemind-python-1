import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Sample dataset
data = {
'Year': [2016, 2017, 2018, 2019, 2020, 2021],
'Sales': [250, 270, 300, 310, 400, 450],
'Profit': [20, 30, 50, 45, 60, 75],
'Market_Share': [10, 12, 15, 17, 19, 22]
}
df1 = pd.DataFrame(data)
plt.figure(figsize=(8, 5))
plt.plot(df1['Year'], df1['Sales'], marker='o', color='g', label='Sales') # markers can be o, |, ^, *
plt.title('Yearly Sales Trend')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.show()
