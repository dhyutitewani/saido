# importing packages 
import assemblyai as aai
import re
# Replace with your API token
aai.settings.api_key = f"9378af6f47394df79bde84c17c4bae50"

# URL of the file to transcribe
def Transcribe(path):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(path)
    return transcript.text
  