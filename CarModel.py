import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize = (20,10))
plt.bar(df2['Car'],df2['Model'],color = 'b',label = 'Model')
plt.title('Car vs Model')
plt.xlabel('Car')
plt.ylabel('Model')
plt.xticks(df2['Car'])
plt.legend()
plt.show()

plt.figure(figsize = (20,10))
plt.bar(df2['Car'],df2['Volume'],color = 'g',label = 'Model')
plt.title('Car vs Model')
plt.xlabel('Car')
plt.ylabel('Volume')
plt.xticks(df2['Car'])
plt.legend()
plt.show()
