import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize = (8,5))
plt.scatter(df2['Car'],df2['Model'],color = 'b',marker = 'o')
plt.title('Car vs Model')
plt.xlabel('Car')
plt.ylabel('Model')
plt.grid(True)
plt.show()

plt.figure(figsize = (8,5))
plt.scatter(df2['Car'],df2['Weight'],color = 'g',marker = '^')
plt.title('Car vs Weight')
plt.xlabel('Car')
plt.ylabel('Weight')
plt.xticks(df2['Car'])
plt.grid(True)
plt.show()
