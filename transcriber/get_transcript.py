# importing packages 
import assemblyai as aai
import re
import os
# Replace with your API token
aai.settings.api_key = os.environ['AAI_APIKEY']

# URL of the file to transcribe
def Transcribe(path):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(path)
    return transcript.text
  