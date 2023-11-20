import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler

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

# Organizing subplots in a 1x3 matrix
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Plotting for 'VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes'
for i, x_col in enumerate(['VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes']):
    x = df[x_col].values.reshape(-1, 1)
    y = df['Calories'].values

    # Fitting linear regression using matrix solution
    coefficients = np.linalg.inv(np.column_stack([np.ones_like(x), x]).T @ np.column_stack([np.ones_like(x), x])) @ np.column_stack([np.ones_like(x), x]).T @ y
    l_coeff, a_coeff = coefficients

    # Model's prediction
    y_pred = np.column_stack([np.ones_like(x), x]) @ coefficients

    r2 = r2_score(y, y_pred)
    MSE = np.mean((y - y_pred)**2)

    # Scatter plot
    axes[i].scatter(x, y, alpha=0.2, color="green")
    
    # Plotting linear regression line
    axes[i].plot(x, l_coeff + a_coeff*x, color="red")

    # Adding labels
    axes[i].set_xlabel(x_col, color="green")
    axes[i].set_ylabel("Calories", color="green")
    
    # Adding title with R² and MSE values
    axes[i].set_title(f"{x_col}\nR² Score: {r2:.4f}  MSE: {MSE:.4f}", fontsize=12)

# Adjusting layout
plt.tight_layout()
plt.show()
