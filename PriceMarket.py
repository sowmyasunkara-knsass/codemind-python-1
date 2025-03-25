import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize = (8,5))
plt.scatter(df['year'],df['sales'],s = df['profit']*2,alpha=0.5,color = 'purple')
plt.title('year vs sales')
plt.xlabel('year')
plt.ylabel('sales')
plt.grid(True)
plt.show()

plt.figure(figsize = (8,5))
plt.scatter(df['prices'],df['market_sales'],s = df['profit']*3,alpha = 0.9,color = 'purple')
plt.title('prices vs market_sales')
plt.xlabel('prices')
plt.ylabel('market_sales')
plt.grid(True)
plt.show()
