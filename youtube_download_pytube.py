# importing the module 
import pytube

# where to save 
SAVE_PATH = "z:/" #to_do 

# link of the video to be downloaded 
url='your link'

try: 
    youtube = pytube.YouTube(url)
    for i in youtube.streams:
        print(i)
    video_tag=input("Please enter video itag number: ")
    audio_tag=input("Please enter audio itag number: ")
    video = youtube.streams.filter(res='2160p')
    videostream = youtube.streams.get_by_itag(video_tag) #video
    audiostream = youtube.streams.get_by_itag(audio_tag) #audio
    print(f"downloading: {videostream}")
    print(f"downloading: {audiostream}")
except: 
    print("Connection Error") #to handle exception 
try: 
    videostream.download('z:/')
    audiostream.download('z:/')
except: 
    print("Some Error!") 
print('Task Completed!') 
