import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Sleep_Efficiency.csv")

age = df["Age"].values.reshape[-1,1]
sleep_efficiency = df["Sleep efficiency"].values

# Cria um modelo de regressão linear
model = LinearRegression()
model.fit(age, sleep_efficiency)

# Faz previsões usando o modelo
regression_line = model.predict(age)

plt.figure()
plt.scatter(age, sleep_efficiency, label="Dados")
plt.plot(age, regression_line, color='red', label='Regressão Linear')

plt.xlabel("Age")
plt.ylabel("Sleep Efficiency")

plt.legend()
plt.show()