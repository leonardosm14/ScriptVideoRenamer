import os

#Diretório
#src = r'DIRETORIO-DA-PASTA'
src = '/home/apv-065/ScriptNomes/ScriptVideoRenamer'

#O primeiro passo é pegar os nomes de todos arquivos .mp4 na pasta
def listarNomes(src):
  
    listaNomes = []
  
    for arquivo in os.listdir(src):
        if arquivo.endswith('.mp4'):
            listaNomes.append(arquivo)
    #ordem alfabética
    #listaNomes = sorted(listaNomes) 
          
    with open('NomesDownload.txt', 'w') as f:
        for nome in listaNomes:
            f.write(nome + '\n')
          
    return
