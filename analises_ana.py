import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("Sleep_Efficiency.csv")

age = df["Sleep duration"].values
sleep_efficiency = df["Sleep efficiency"].values

plt.figure()
plt.scatter(age, sleep_efficiency)
plt.xlabel("Age")
plt.ylabel("Sleep Efficiency")

plt.show()