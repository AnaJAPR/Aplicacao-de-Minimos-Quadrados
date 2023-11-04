from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource
import pandas as pd
from bokeh.io.export import export_png

# Ler o arquivo excel
df = pd.read_excel('planilha_brasil.xlsx')

# Obter as datas do DataFrame
datas = df.iloc[:, 0]

# Converter as datas para o formato desejado
datas_formatadas = datas.dt.strftime('%b/%y')

# Substituir a primeira coluna pelas datas formatadas
df.iloc[:, 0] = datas_formatadas

# Extraindo as colunas "Data" e "Taxa"
data = df['Data']
taxa = df['Taxa']

# Criar uma fonte de dados para o Bokeh
source = ColumnDataSource(data={'data': data, 'taxa': taxa})

# Criar a figura
p = figure(title='Gráfico de Dispersão', x_axis_label='Data', y_axis_label='Taxa', x_range=datas_formatadas.tolist())

# Adicionar o gráfico de dispersão
p.scatter('data', 'taxa', source=source, size=8, color='blue', alpha=0.5)

# Rotacionar os rótulos do eixo x
p.xaxis.major_label_orientation = 3.14 / 4

# Mostrar o gráfico

show(p)'''
