from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource
import pandas as pd
import numpy as np

# Ler os dados do arquivo Excel
df = pd.read_csv('2021.csv')

# Calcular os coeficientes da reta de regressão usando o método dos mínimos quadrados
x = df['mathematics_score']
y = df['literature_score']
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

# Criar uma fonte de dados para o gráfico
source = ColumnDataSource(df)

# Criar o gráfico de dispersão
p = figure(title='Notas', x_axis_label='Matemática', y_axis_label='Literatura')

# Adicionar os pontos de dispersão
p.circle(x='mathematics_score', y='literature_score', source=source, size=10, color='blue', alpha=0.5)

# Adicionar a reta de regressão
p.line(x, m*x + c, line_color='red', line_width=2, legend_label=f'Reta de Regressão (m={m:.2f}, c={c:.2f})')

# Exibir o gráfico
show(p)

#Deu problema na regressão