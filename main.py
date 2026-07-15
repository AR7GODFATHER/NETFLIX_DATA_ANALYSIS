import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("netflix_titles.csv")
df=df.dropna()
print(df.isnull().sum())