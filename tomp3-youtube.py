"""
Aplicativo para baixar musica do youtube
Desenvolvido por Daniel Catto

bibliotecas requeridas pytube, moviepy

"""

from pytube import Playlist, YouTube

from moviepy.editor import *
import shutil

def cabecalho():
    print("################################")
    print("Baixar videos YouTube")
    print("")
    print("Escolha as opções")
    print("1 - Baixar playlist")
    print("2 - Converter para MP3")
    print("3 - Baixar video individual")
    print("5 - Fechar aplicação")
    print("################################")

def baixar_video():
    url = "https://www.youtube.com/watch?v=irzOMH7GcnQ"#input("cole o aqui o endereço da playlist")
    
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download()
    print(video.title)
    
    

def baixar_video_playlist():

    Playlist_url = input("cole o aqui o endereço da playlist")
    playlist = Playlist(Playlist_url)
    tamanho = len(playlist)
    
    for url in playlist:
        try:
            video = YouTube(url)
            print(str(tamanho) + " - " + video.title + " - " + url)
            stream = video.streams.get_highest_resolution()
            stream.download()
            
            tamanho -= 1
            
            
        except:
            print(str(tamanho), ": Oops! Video privado ou não permitido na sua região! ...")
            tamanho -= 1

def converte_to_mp3():
    cwd = os.getcwd()
    som = cwd+'/mp3/'
    mp4 = cwd+'/videos/'
    musicas = os.listdir(cwd)
    tamanho = len(musicas)
    print(cwd)
    print(som)
    print(mp4)
    print(musicas)
        
    for musica in musicas:
        if(musica[-4:] == ".mp4"):
            musica_sprit = musica[0:-4]
            print( musica_sprit+".mp3")
            
            video = VideoFileClip(os.path.join(musica))         
            video.audio.write_audiofile(os.path.join(som, musica_sprit+".mp3"))
            shutil.move(musica, mp4 )
            tamanho -= 1
            print(musica, video)
        else:
            print(musica)
        

op = 0
while True: 
    cabecalho()
    op = int(input(">>>"))
    if(op == 5):
        break
    elif (op == 1):
        baixar_video_playlist()
    elif(op == 2):
        converte_to_mp3()
    
    elif (op == 3):
        baixar_video()
        
    elif (op == 5):
        print("Fim")
        break


