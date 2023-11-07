import gradio as gr
import json
import time

from src.model.modelv2 import initialize_qa_chain, ask_question  # Import functions from your updated model file

with open('/home/exvynai/code/dev/saido/src/model/transcriptions.json', 'r') as json_file:
    data = json.load(json_file)

# Initialize the QA chain and chat_history for the model
qa_chain = initialize_qa_chain(data)
model_chat_history = []

def gradio_chatbot():
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot()
        msg = gr.Textbox()
        clear = gr.ClearButton([msg, chatbot])

        def respond(message, chat_history):
            # Use the Gradio chat history for Gradio interactions
            bot_message = ask_question(qa_chain, model_chat_history, message)  # Use the model chat history for model interactions
            chat_history.append((message, bot_message))  # Append user message to Gradio chat history
            time.sleep(2)
            return "", chat_history

        msg.submit(respond, [msg, chatbot], [msg, chatbot])

        demo.launch()

if __name__ == "__main__":
    gradio_chatbot()
