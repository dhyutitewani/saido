## importing packages 
from Get_YTAudio import *
from Get_Transcript import *
import os

if __name__  ==  "__main__": 
    #getting url
    print("Enter the Youtube URL:")
    url = Get_url()
    #getting audio 
    print("Getting Audio...")
    Audio_file = Get_Audio(url)
    # result of success 
    print("'"+url.title +"'"+ " has been successfully downloaded.")
    #getting transcibed text from audio
    print("Converting audio to text...")
    #getting the path of audio file
    path = Get_Path(Audio_file)
    #transcription
    transcript = Transcribe(path)
    #printing transcribed text
    print(transcript)
    #deleting the audio file
    print("successfull transcription of: "+url.title+".mp4 into text")
    os.remove(Audio_file)
    print("***Audio file deleted***")



    