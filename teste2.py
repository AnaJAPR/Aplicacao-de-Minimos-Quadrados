import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

def plot_scatter_with_regression_grid(df, x_cols, y_col):
    df_subset = df[x_cols + [y_col]].dropna()

    # Criando um gráfico com subplots organizados em uma matriz 1x3
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Iterando sobre as colunas de interesse
    for i, x_col in enumerate(x_cols):
        # Criando o scatter plot para cada coluna em relação à coluna Y
        sns.scatterplot(x=x_col, y=y_col, data=df_subset, ax=axes[i], color='orange')

        # Ajustando o modelo de regressão linear
        X = df_subset[x_col].values.reshape(-1, 1)
        y = df_subset[y_col].values
        model = LinearRegression().fit(X, y)

        # Traçando a linha de regressão
        axes[i].plot(X, model.predict(X), color='purple')

        # Adicionando rótulos
        axes[i].set_xlabel(x_col)
        axes[i].set_ylabel(y_col)

        # Ajustando cores dos eixos
        axes[i].xaxis.label.set_color('blue')
        axes[i].yaxis.label.set_color('green')

        # Ajustando cor do fundo
        axes[i].set_facecolor('lightgray')

    # Ajustando layout
    plt.tight_layout()

    # Adicionando título
    fig.suptitle(f'Scatter Plots com Regressão Linear para {y_col} e {", ".join(x_cols)}', fontsize=16, y=1.02)

    return fig

# Carregando os dados do arquivo CSV em um DataFrame
df = pd.read_csv('dailyactivity_v3.csv')

# Chamando a função com diferentes combinações de colunas
fig_1 = plot_scatter_with_regression_grid(df, ['VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes'], 'Calories')
#fig_2 = plot_scatter_with_regression_grid(df, ['VeryActiveDistance', 'ModeratelyActiveDistance', 'LightActiveDistance'], 'Calories')
#fig_3 = plot_scatter_with_regression_grid(df, ['TotalSteps', 'TotalDistance', 'TotalMinutesActive'], 'Calories')
plt.show()

'''

##########################    MINUTOS SEDENTARIOS   #################

# Selecionando as colunas de interesse
columns_of_interest = ['SedentaryMinutes', 'Calories']

df_minutes_type = df[columns_of_interest].dropna()

# Criando o scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='SedentaryMinutes', y='Calories', data=df_minutes_type)

# Ajustando o modelo de regressão linear
X = df_minutes_type['SedentaryMinutes'].values.reshape(-1, 1)
y = df_minutes_type['Calories'].values
model = LinearRegression().fit(X, y)

# Traçando a linha de regressão
plt.plot(X, model.predict(X), color='red')

# Adicionando rótulos e título
plt.xlabel('SedentaryMinutes')
plt.ylabel('Calories')
plt.title('Scatter Plot com Regressão Linear para Calories e SedentaryMinutes')

plt.show()
'''