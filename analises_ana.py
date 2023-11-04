import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from sklearn import linear_model

data = pd.read_csv("Sleep_Efficiency.csv").dropna()

age = data["age"].values
sleep_efficiecy = data["Sleep efficiency"].values

plt.figure()
plt.scatter(age, sleep_efficiecy)
plt.xlabel("Age")
plt.ylabel("Sleep Efficiency")