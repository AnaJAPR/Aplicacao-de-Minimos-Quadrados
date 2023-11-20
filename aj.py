# importing necessary libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Reading data from csv and dropping null values
df = pd.read_csv("dailyactivity_v3.csv").dropna()

# Identification of the ID column so as not to modify this column later
coluna_id = "Id"

# Selection of numeric columns, except the ID column
colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns
colunas_numericas = colunas_numericas.drop(coluna_id)

# MinMaxScaler initialization
scaler = MinMaxScaler()

# Normalization of all numeric columns
for coluna in colunas_numericas:
    df[coluna] = scaler.fit_transform(df[[coluna]])

x1 = df["LightlyActiveMinutes"].values.reshape(-1,1)
y1 = df["LightActiveDistance"].values

# Adding a column of 1s to represent the linear term
X_1 = np.column_stack([np.ones_like(x1), x1])


# Fitting the linear regression using matrix solution
coefficients_1 = np.linalg.inv(X_1.T @ X_1) @ X_1.T @ y1

# Angular and linear coefficients
l1_coeff, a1_coeff = coefficients_1

# Model's prediction
y1_pred = X_1 @ coefficients_1

r2_1 = r2_score(y1, y1_pred)
MSE_1 = np.mean((y1 - y1_pred)**2)
print(f"1-R² Score: {r2_1:.4f}            MSE: {MSE_1}")

# Plotting 1
plt.scatter(x1, y1, alpha=0.2, color="green")
plt.plot(x1, l1_coeff + a1_coeff*x1, color="red") # line representing linear regression

plt.xlabel("Lightly Active Minutes", color="green")
plt.ylabel("Light Active Distance", color="green"); # we use ";" to avoid printing the output

# code just to check the data's concentration at the beginning of the graph 1
x1 = df["LightlyActiveMinutes"].values
y1 = df["LightActiveDistance"].values
plt.boxplot([x1,y1]); # we use ";" to avoid printing the output