import os
from moviepy.editor import *
import shutil
cwd = os.getcwd()
som = cwd+'/mp3/'
mp4 = cwd+'/videos/'
musicas = os.listdir(cwd)
tamanho = len(musicas)

for musica in musicas:
    
    if(musica[-4:] == ".mp4"):
        musica_sprit = musica[0:-4]
        print(tamanho, ": ", musica_sprit+".mp3")
        
        video = VideoFileClip(os.path.join(musica))         
        video.audio.write_audiofile(os.path.join(som, musica_sprit+".mp3"))
        shutil.move(musica, mp4 )
        tamanho -= 1
        print(musica, video)
    else:
        print(musica)

    