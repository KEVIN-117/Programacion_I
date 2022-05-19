from pytube import YouTube
link = input("Introdruced a link: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()