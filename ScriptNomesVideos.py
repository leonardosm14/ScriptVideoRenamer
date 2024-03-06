import os
import pandas as pd
from ScriptPegarNomesDownload import src, listarNomes

#Adicionando todos nomes .mp4 no arquivo de texto NomesDownload
listarNomes(src)

# Carregando os nomes dos vídeos de dois arquivos de texto
nomes_videos = pd.read_csv('NomesTeste.txt', header=None, names=['Nomes_Videos'])
nomes_reais = pd.read_csv('NomesDownload.txt', header=None, names=['Nomes_Reais'])

# Criação do DataFrame
dataframe = pd.concat([nomes_videos, nomes_reais], axis=1)

for index, row in dataframe.iterrows():
    nome_video = row['Nomes_Videos']
    nome_real = row['Nomes_Reais']
  
    os.rename(fr'{src}\{nome_real}', fr'{src}\{nome_video}.mp4')
    print(f'O arquivo foi renomeado de "{nome_real}" para "{nome_video}"')

print(dataframe)
