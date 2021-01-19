from pytube import Playlist, YouTube
import os
from moviepy.editor import *
import shutil


def baixar_video():

    Playlist_url = input("cole o aqui o endereço da playlist")
    playlist = Playlist(Playlist_url)
    tamanho = len(playlist)
    print(tamanho)
    for url in playlist:
        try:
            video = YouTube(url)
            print(str(tamanho) + " " + url)
            stream = video.streams.get_highest_resolution()
            stream.download()
            tamanho -= 1
            
            
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

def converte_to_mp3():
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


a = 0
while True:
    print("Baixar videos no youtube\nDigite uma opção: ")
    numero = input(">>>")
    num_int = int(numero)
    if (num_int != 5) or (numero == ""):
        print(num_int)
    else:
        break
                