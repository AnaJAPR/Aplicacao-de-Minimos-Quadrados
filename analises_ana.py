import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from sklearn import linear_model

data = pd.read_csv("Sleep_Efficiency.csv")

age = data["Age"].values
sleep_efficiency = data["Sleep efficiency"].values

plt.figure()
plt.scatter(age, sleep_efficiency)
plt.xlabel("Age")
plt.ylabel("Sleep Efficiency")