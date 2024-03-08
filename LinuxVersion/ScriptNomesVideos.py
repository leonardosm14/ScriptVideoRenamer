import os
import pandas as pd
from ScriptPegarNomesDownload import src, listarNomes

# Adicionando todos os nomes .mp4 no arquivo de texto NomesDownload
listarNomes(src)

# Carregando os nomes dos vídeos de dois arquivos de texto
with open('NomesTeste.txt', 'r') as file1, open('NomesDownload.txt', 'r') as file2:
    nomes_videos = file1.readlines()
    nomes_reais = file2.readlines()

# Remove espaços
nomes_videos = [nome.strip() for nome in nomes_videos]
nomes_reais = [nome.strip() for nome in nomes_reais]

# Criação do DataFrame
dataframe = pd.DataFrame({'Nomes_Videos': nomes_videos, 'Nomes_Reais': nomes_reais})

# Loop
for index, row in dataframe.iterrows():
    nome_video = row['Nomes_Videos']
    nome_real = row['Nomes_Reais']

    os.rename(f'{src}/{nome_real}', f'{src}/{nome_video}.mp4')
    print(f'O arquivo foi renomeado de "{nome_real}.mp4" para "{nome_video}.mp4"')

print(dataframe)
