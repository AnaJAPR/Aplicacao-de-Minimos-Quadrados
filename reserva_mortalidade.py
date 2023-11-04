from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
import pandas as pd
from bokeh.io.export import export_png
'''
# Ler o arquivo excel
df = pd.read_excel('taxa_mortalidade_brasil.xlsx')
print(df)

# Criar uma fonte de dados para o gráfico
source = ColumnDataSource(df)

# Criar o gráfico de dispersão
p = figure(title='Taxa de Mortalidade ao longo dos Anos', x_axis_label='Ano', y_axis_label='Taxa de Mortalidade')

# Adicionar os pontos de dispersão
p.circle(x='ano', y='taxa_mortalidade', source=source, size=10, color='blue', alpha=0.5)

# Exibir o gráfico
show(p)
'''

from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource
import pandas as pd
import numpy as np

# Ler os dados do arquivo Excel
df = pd.read_excel('taxa_mortalidade_brasil.xlsx')

# Calcular os coeficientes da reta de regressão usando o método dos mínimos quadrados
x = df['ano']
y = df['taxa_mortalidade']
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

# Criar uma fonte de dados para o gráfico
source = ColumnDataSource(df)

# Criar o gráfico de dispersão
p = figure(title='Taxa de Mortalidade ao longo dos Anos', x_axis_label='Ano', y_axis_label='Taxa de Mortalidade')

# Adicionar os pontos de dispersão
p.circle(x='ano', y='taxa_mortalidade', source=source, size=10, color='blue', alpha=0.5)

# Adicionar a reta de regressão
p.line(x, m*x + c, line_color='red', line_width=2, legend_label=f'Reta de Regressão (m={m:.2f}, c={c:.2f})')

# Exibir o gráfico
show(p)


