import os

#Diretório
src = r'DIRETORIO-DA-PASTA'

#O primeiro passo é pegar os nomes de todos arquivos .mp4 na pasta
def listarNomes(src):
  
    listaNomes = []
  
    for arquivo in os.listdir(src):
        if arquivo.endswith('.mp4'):
            listaNomes.append(arquivo)
          
    with open('NomesDownload.txt', 'w') as f:
        for nome in listaNomes:
            f.write(nome + '\n')
          
    return
