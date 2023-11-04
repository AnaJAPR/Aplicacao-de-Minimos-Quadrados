import pandas as pd

# Ler o arquivo CSV
df = pd.read_excel('series_historicas.xlsx')

print(df)
'''
# Transpor o DataFrame
df_transposto = df.transpose()

# Definir a primeira linha como cabeçalho
df_transposto.columns = df_transposto.iloc[0]

# Remover a primeira linha (que agora é o cabeçalho)
df_transposto = df_transposto[1:]

# Resetar os índices
df_transposto = df_transposto.reset_index(drop=True)

# Mostrar o DataFrame transposto
print(df_transposto)
'''
