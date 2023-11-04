import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sleep_Efficiency.csv")

age = df["Age"].values
sleep_efficiency = df["Sleep efficiency"].values

plt.figure()
plt.scatter(age, sleep_efficiency)



