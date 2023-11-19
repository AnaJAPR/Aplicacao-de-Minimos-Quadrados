# Importando as bibliotecas necessárias
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler

# Lendo dados do arquivo CSV e removendo valores nulos
# df = pd.read_csv("Sleep_Efficiency.csv").dropna()

# Criando vetores x e y com valores das colunas Deep sleep percentage e Light sleep percentage
# O reshape ajusta os valores em uma matriz bidimensional para futiplas multiplicações
# x = df["Deep sleep percentage"].values.reshape(-1,1) 
# y = df["Light sleep percentage"].values

# Lendo dados do arquivo CSV e removendo valores nulos
df = pd.read_csv("dailyactivity_v3.csv").dropna()

# plt.scatter(x,y, alpha=0.3)
# plt.boxplot([x,y])


# Identificação da coluna de ID para não modificá-la posteriormente
coluna_id = "Id"

# Seleção de colunas numéricas, excluindo a coluna de ID
colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns
colunas_numericas = colunas_numericas.drop(coluna_id)

# Inicialização do MinMaxScaler
scaler = MinMaxScaler()

# Normalização de todas as colunas numéricas
for coluna in colunas_numericas:
    df[coluna] = scaler.fit_transform(df[[coluna]])

# Visualização dos dados normalizados
print(df.head)

# Código para verificar se todos os valores no banco de dados estão normalizados
'''
lista = []
for coluna in colunas_numericas:
    for valor in df[coluna].values:
        if valor < 0 or valor > 1:
            lista.append((coluna, valor)) 

print(lista)
'''

# Criando vetores x e y com valores das colunas do banco de dados

# x = df["TotalMinutesActive"].values.reshape(-1,1)   # para usar, precisamos explicar a razão da concentração de dados no final do gráfico
# y = df["SedentaryMinutes"].values

x = df["LightlyActiveMinutes"].values.reshape(-1,1)
y = df["LightActiveDistance"].values

# Adicionando uma coluna de 1s para representar o termo linear
X = np.column_stack([np.ones_like(x), x])

# Ajustando a regressão linear usando a solução matricial
coefficients = np.linalg.inv(X.T @ X) @ X.T @ y

# Coeficientes angular e linear
l_coeff, a_coeff = coefficients

# Predição do modelo
y_pred = X @ coefficients

# Coeficiente r², usado para verificar a precisão da regressão linear
r2 = r2_score(y, y_pred)
print(f"R^2 Score: {r2:.4f}")

# Plotando
plt.scatter(x, y, alpha=0.2, color="green")
plt.plot(x, l_coeff + a_coeff*x, color="red") # linha representando a regressão linear

# Esta linha serve para representar um ponto específico no gráfico quando necessário ou importante
# plt.scatter(0, l_coeff + a_coeff*2.5, color='lightgreen', s = 20)
