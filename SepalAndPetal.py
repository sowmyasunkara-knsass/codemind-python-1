import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset('iris')
plt.figure(figsize = (8,5))
sns.scatterplot(data=iris,x = 'sepal_length',y = 'sepal_width',hue = 'species',style = 'species',palette = 'deep')
plt.title('sepal length vs sepal width by species')
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.grid(True)
plt.show()
