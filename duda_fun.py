import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

def plot_scatter_with_regression_grid(df, x_cols, y_col):
    df_subset = df[x_cols + [y_col]].dropna()

    # Criando um gráfico com subplots organizados em uma matriz 1x3
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Iterando sobre as colunas de interesse
    for i, x_col in enumerate(x_cols):
        # Criando o scatter plot para cada coluna em relação à coluna Y
        sns.scatterplot(x=x_col, y=y_col, data=df_subset, ax=axes[i], color='#3CAA9F', s=50, alpha=0.5)

        # Ajustando o modelo de regressão linear
        X = df_subset[x_col].values.reshape(-1, 1)
        y = df_subset[y_col].values
        model = LinearRegression().fit(X, y)

        # Traçando a linha de regressão
        axes[i].plot(X, model.predict(X), color='#8A4525')

        # Adicionando rótulos
        axes[i].set_xlabel(x_col, fontsize=12)
        axes[i].set_ylabel(y_col, fontsize=12)

        # Ajustando cores dos eixos
        axes[i].xaxis.label.set_color('black')
        axes[i].yaxis.label.set_color('black')

        # Ajustando cor do fundo
        axes[i].set_facecolor('#FFD79F')

    # Ajustando layout
    plt.tight_layout()

    # Ajustando espaço entre os gráficos e a borda da imagem
    plt.subplots_adjust(wspace=0.24, top=0.9)  # Ajuste o valor conforme necessário

    # Adicionando título com maior espaço entre o título e os gráficos
    fig.suptitle(f'Linear Regression for {y_col} e {", ".join(x_cols)}', fontsize=16)

    return fig

# Carregando os dados do arquivo CSV em um DataFrame
df = pd.read_csv('dailyactivity_v3.csv')

# Chamando a função com diferentes combinações de colunas
fig_1 = plot_scatter_with_regression_grid(df, ['VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes'], 'Calories')
fig_2 = plot_scatter_with_regression_grid(df, ['VeryActiveDistance', 'ModeratelyActiveDistance', 'LightActiveDistance'], 'Calories')
fig_3 = plot_scatter_with_regression_grid(df, ['TotalSteps', 'TotalDistance', 'TotalMinutesActive'], 'Calories')
plt.show()