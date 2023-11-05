import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


musicas= pd.read_excel('spotify-2023.xlsx')
print(musicas)

'''
sucessos=[]

for item in musicas['in_spotify_playlists']:
  if item not in sucessos:
    sucessos.append(item)
sucessos

ranking=[] # Retorna os maiores números de playlists

for num in range(10):
  valor_max=max(sucessos)
  ranking.append(valor_max)
  sucessos.remove(valor_max)
ranking
'''