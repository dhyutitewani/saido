from pytube import YouTube
import os
import assemblyai as aai
import dotenv

aai.settings.api_key = dotenv.get_key(dotenv.find_dotenv(), "AAI_APIKEY")


def transcribe_youtube_video(url):
    yt = YouTube(url)

    audio_stream = yt.streams.filter(only_audio=True).first()

    if audio_stream:
        audio_file = audio_stream.download("audio")

        audio_path = os.path.join("./audio", os.path.basename(audio_file))

        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(audio_path).text

        os.remove(audio_path)

        return transcript
    else:
        return "No suitable audio stream found for transcription."


if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=mVKAyw0xqxw&t=6s"
    result = transcribe_youtube_video(youtube_url)
    print(result)
