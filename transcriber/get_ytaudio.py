# importing packages 
from pytube import YouTube 
import os 

# url input from user 
def Get_url(url):
 return YouTube(url) 
  
# extract only audio and download the file 
def Get_Audio(url):
    video = url.streams.filter(only_audio=True).first() 
    Audio_file = video.download('Audio') 
    return Audio_file

#returns youtube audio path
def Get_Path(Audio_file):
   x = os.path.basename(Audio_file)
   print("paht is:", x)
   path = "./Audio/"+x
   return path
