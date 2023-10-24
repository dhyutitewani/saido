# importing packages 
import assemblyai as aai
import re
# Replace with your API token
aai.settings.api_key = f"<API- Key>"

# URL of the file to transcribe
def Transcribe(path):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(path)
    return transcript.text
  