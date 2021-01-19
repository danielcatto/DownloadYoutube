import os
from moviepy.editor import *

cwd = os.getcwd()
musicas = os.listdir(cwd)
print(musicas)

lista = os.listdir(cwd+"/musicas")
print(lista)