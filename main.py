from pytube import Playlist, YouTube


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
        
    