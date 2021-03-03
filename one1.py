from pytube import YouTube
Link = input("write video link: ")
video = YouTube(Link)
video.streams.get_highest_resolution().download(output_path="/c:")
print(video)