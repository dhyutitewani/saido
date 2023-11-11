# Saido

Saido is a conversational chatbot project designed to answer questions about YouTube videos, transcribe audio, and summarize text.

## Features

- Chatbot functionality for answering questions based on YouTube video content.
- Transcription of audio from YouTube videos.
- Summarization of textual content.

## Installation

### Prerequisites
- Python 3.6 or higher
- PyTorch
- transformers library
- gradio library
- pytube library
- assemblyai library

### Installation Steps
1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up the environment variables, including `AAI_APIKEY` for the AssemblyAI API.

## Usage

### Webapp
- Launch the Webapp by running `python -m src.webapp.webapp`

### Chatbot
- Run `python -m src.model.modelv2`.

### Transcribing YouTube Videos
- Run `python src.text_processing.transcriber`.

### Summarizing Text
- Run `python src.text_processing.summarizer`.

## Contributing

Contributions to Saido are welcomed! Feel free to:
- Fork the repository and create a pull request.
- Report bugs or request new features using the Issues tab.