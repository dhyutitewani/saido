import json
import os

from get_ytaudio import *
from get_transcript import *

if __name__ == "__main__":
    # Prompt for the input file containing a list of YouTube URLs
    input_file = input("Enter the name of the file with YouTube URLs: ")

    # Define the output JSON file for storing transcriptions
    output_file = "transcriptions.json"
    
    transcriptions = []  # List to store transcriptions

    with open(input_file, 'r') as url_file:
        urls = url_file.read().splitlines()

    for url in urls:

        original_url = url
        # Convert to Youtube URL
        url = Get_url(url)
        # Getting audio
        print("Getting Audio for:", url)
        audio_file = Get_Audio(url)
        
        # Getting the path of the audio file
        path = Get_Path(audio_file)
        
        # Transcription
        transcript = Transcribe(path)
        transcriptions.append({
            'url': original_url,
            'transcript': transcript
        })
        
        # Deleting the audio file
        os.remove(audio_file)
        print("Successfully transcribed:", url)

    # Write transcriptions to a JSON file
    with open(output_file, 'w') as json_file:
        json.dump(transcriptions, json_file, indent=4)

    print(f"Transcriptions have been saved to '{output_file}' in JSON format.")
