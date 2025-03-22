import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
     'year': [2021,2022,2023,2024,2025,2026],
     'sales': [300,400,150,200,350,250],
     'profit': [35,20,25,23,10,15],
     'market_sales': [15,10,9,22,13,20]
}
df = pd.DataFrame(data)
print(df)
