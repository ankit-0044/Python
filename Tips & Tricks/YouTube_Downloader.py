# YouTube Downloader
from pytube import *

link = input("Enter Your Youtube URL: ")
print()
yt = YouTube(link)
videos = yt.streams.all()       # Show all the format available for the video

video = list(enumerate(videos))         # Index all the format in list starting with zero

for i in video:         # Print all the available format with proper index
    print(i)
print()
print("Enter the desired option to download the formate.")
dn_option = int(input("Enter the your option: "))       # Ask the user which format he wanted to download

dn_video = videos[dn_option]
dn_video.download()         # For downloading 

print("Download Successful")
