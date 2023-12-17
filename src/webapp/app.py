import gradio as gr
import time
from src.model.modelv2 import initialize_qa_chain, ask_question
from src.text_processing.transcriber import transcribe_youtube_video

# Initialize the QA chain and chat_history for the model
model_chat_history = []
qa_chain = None

def gradio_chatbot():
    with gr.Blocks() as demo:
        # Transcription block
        url = gr.Textbox(label="url")
        transcription_text = gr.Textbox(label="transcription")

        # Chatbot block
        chatbot = gr.Chatbot()
        msg = gr.Textbox()
        clear = gr.ClearButton([url, transcription_text, msg, chatbot])

        def respond_transcription(url, transcription_text):
            global qa_chain
            transcription_text = transcribe_youtube_video(url)
            qa_chain = initialize_qa_chain(transcription_text)
            time.sleep(2)
            return url, transcription_text, qa_chain
        

        def respond_chat(message, chat_history):
            global qa_chain
            if qa_chain is None:
                # Handle the case where qa_chain is not initialized
                return "Error: QA chain not initialized", chat_history

            bot_message = ask_question(qa_chain, message)
            chat_history.append((message, bot_message))
            time.sleep(2)
            return "", chat_history

        url.submit(respond_transcription, [url, transcription_text], [url, transcription_text])
        msg.submit(respond_chat, [msg, chatbot], [msg, chatbot])
        demo.launch()

if __name__ == "__main__":
    gradio_chatbot()
