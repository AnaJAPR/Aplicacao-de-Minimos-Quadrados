import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
df = pd.read_excel('planilha_brasil.xlsx')
# Obter as datas do DataFrame
datas = df.iloc[:, 0]
# Converter as datas para o formato desejado
datas_formatadas = datas.dt.strftime('%b/%y')
# Substituir a primeira coluna pelas datas formatadas
df.iloc[:, 0] = datas_formatadas
print(df)

plt.scatter(df.iloc[:, 0], df.iloc[:, 1])
# Adicionar rótulos
plt.xlabel('Eixo X (Datas)')
plt.ylabel('Eixo Y (Valores)')

# Exibir o gráfico
plt.show()