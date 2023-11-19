import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
'''
LoggedActivitiesDistance	
SedentaryActiveDistance	
SedentaryMinutes	
Calories 
'''
##########MINUTES################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Carregando os dados do arquivo CSV em um DataFrame
df = pd.read_csv('dailyactivity_v3.csv')

# Selecionando as colunas de interesse
columns_of_interest = ['VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes', 'Calories']

df_subset = df[columns_of_interest].dropna()

# Criando três gráficos separados
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for i, col in enumerate(['VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes']):
    # Criando o scatter plot para cada tipo de minutos em relação às calorias
    sns.scatterplot(x=col, y='Calories', data=df_subset, ax=axes[i])

    # Ajustando o modelo de regressão linear
    X = df_subset[col].values.reshape(-1, 1)
    y = df_subset['Calories'].values
    model = LinearRegression().fit(X, y)

    # Traçando a linha de regressão
    axes[i].plot(X, model.predict(X), color='red')

    # Adicionando rótulos
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Calories')

# Ajustando layout
plt.tight_layout()

# Adicionando título
fig.suptitle('Scatter Plots com Regressão Linear para Calorias e Tipos de Minutos', fontsize=16)

plt.show()



###########DISTANCE##############

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Carregando os dados do arquivo CSV em um DataFrame
df = pd.read_csv('dailyactivity_v3.csv')

# Selecionando as colunas de interesse
columns_of_interest = [
    'VeryActiveDistance', 'ModeratelyActiveDistance', 'LightActiveDistance', 'SedentaryActiveDistance', 'Calories'
]

df_subset = df[columns_of_interest].dropna()

# Criando três gráficos separados
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for i, col in enumerate(['VeryActiveDistance', 'ModeratelyActiveDistance', 'LightActiveDistance']):
    # Criando o scatter plot para cada tipo de distância em relação às calorias
    sns.scatterplot(x=col, y='Calories', data=df_subset, ax=axes[i])

    # Ajustando o modelo de regressão linear
    X = df_subset[col].values.reshape(-1, 1)
    y = df_subset['Calories'].values
    model = LinearRegression().fit(X, y)

    # Traçando a linha de regressão
    axes[i].plot(X, model.predict(X), color='red')

    # Adicionando rótulos
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Calories')

# Ajustando layout
plt.tight_layout()

# Adicionando título
fig.suptitle('Scatter Plots com Regressão Linear para Calorias e Tipos de Distância', fontsize=16)

plt.show()

###########TOTAL DISTANCE, STEP, MINUTES ####################33

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Carregando os dados do arquivo CSV em um DataFrame
df = pd.read_csv('dailyactivity_v3.csv')

# Selecionando as colunas de interesse
columns_of_interest = ['TotalSteps', 'TotalDistance', 'TotalMinutesActive', 'Calories']

df_subset = df[columns_of_interest].dropna()

# Criando um gráfico com subplots organizados em uma matriz 1x3
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Iterando sobre as colunas de interesse
for i, col in enumerate(['TotalSteps', 'TotalDistance', 'TotalMinutesActive']):
    # Criando o scatter plot para cada coluna em relação às calorias
    sns.scatterplot(x=col, y='Calories', data=df_subset, ax=axes[i])

    # Ajustando o modelo de regressão linear
    X = df_subset[col].values.reshape(-1, 1)
    y = df_subset['Calories'].values
    model = LinearRegression().fit(X, y)

    # Traçando a linha de regressão
    axes[i].plot(X, model.predict(X), color='red')

    # Adicionando rótulos
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Calories')

# Ajustando layout
plt.tight_layout()

# Adicionando título
fig.suptitle('Scatter Plots com Regressão Linear para Calorias e TotalSteps/TotalDistance/TotalMinutesActive', fontsize=16)

plt.show()


##########################    MINUTOS SEDENTARIOS   #################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Carregando os dados do arquivo CSV em um DataFrame
df = pd.read_csv('dailyactivity_v3.csv')

# Selecionando as colunas de interesse
columns_of_interest = ['SedentaryMinutes', 'Calories']

df_subset = df[columns_of_interest].dropna()

# Criando o scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='SedentaryMinutes', y='Calories', data=df_subset)

# Ajustando o modelo de regressão linear
X = df_subset['SedentaryMinutes'].values.reshape(-1, 1)
y = df_subset['Calories'].values
model = LinearRegression().fit(X, y)

# Traçando a linha de regressão
plt.plot(X, model.predict(X), color='red')

# Adicionando rótulos e título
plt.xlabel('SedentaryMinutes')
plt.ylabel('Calories')
plt.title('Scatter Plot com Regressão Linear para Calories e SedentaryMinutes')

plt.show()
