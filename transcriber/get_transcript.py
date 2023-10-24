# importing packages 
import assemblyai as aai
import re
import dotenv


aai.settings.api_key = dotenv.get_key(dotenv.find_dotenv(), "AAI_APIKEY")
# URL of the file to transcribe
def Transcribe(path):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(path)
    return transcript.text
  