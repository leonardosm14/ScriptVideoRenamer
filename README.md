Este é um script básico em Python para a alteração de nomes de vídeos baixados, que geralmente são aleatórios, para nomes selecionados. Primeiramente, é importante se certificar que os vídeos estão na mesma ordem que irão receber os nomes e que todos arquivos estejam na mesma pasta que os scripts.

Para rodá-lo, é necessário ter o pandas instalado, além do Python.

1) Instalação do Pandas:  
   a) No Windows: `pip install pandas`  
   b) No Linux (Ubuntu) ou Mac: `pip3 install pandas`  
   
2) Além dos arquivos .mp4 que irão ter os nomes trocados, é necessário ter dois arquivos de texto na pasta:  
   a) .txt (ou .csv) om os nomes, em ordem, que os vídeos irão receber  
   b) .txt (ou .csv) VAZIO para que o script "ScriptPegarNomesDownload.py" consiga transcrever o nome dos arquivos .mp4
   
3) Tendo feito estes procedimentos, abra o terminal neste diretório e execute o código:  
   a) No Windows: `python ScriptNomesVideos.py`  
   b) No Linux (Ubuntu) ou Mac: `python3 ScriptNomesVideos.py`

OBS: É importante, também, se atentar aos nomes dos arquivos .txt ou .csv criados, para que possam ser alterados no script
