import sys
import json
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceHub

def model():
    # Load data from a JSON file
    try:
        with open('./transcriber/transcriptions.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print("Error: The JSON file was not found. Please ensure the file path is correct.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Failed to parse the JSON file. Ensure it's valid JSON.")
        sys.exit(1)

    # Configuration
    repo_id = "mistralai/Mistral-7B-v0.1"
    huggingfacehub_api_token = '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'
    model_kwargs = {"temperature": 0.5, "max_new_tokens": 100}

    try:
        llm = HuggingFaceHub(huggingfacehub_api_token=huggingfacehub_api_token, repo_id=repo_id, model_kwargs=model_kwargs)
    except Exception as e:
        print(f"Error: Failed to initialize HuggingFaceHub. {str(e)}")
        sys.exit(1)

    
    # Loop through data
    for text in data:
        embeddings = HuggingFaceEmbeddings()
        db = Chroma.from_texts(text, embeddings)
        retriever = db.as_retriever(search_kwargs={'k': 2})
        qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever, return_source_documents=True)
        chat_history = []

        while True:
            query = input('Prompt: ')
            if query.lower() in ["exit", "quit", "q"]:
                print('Exiting')
                sys.exit()

            result = qa_chain({'question': query, 'chat_history': chat_history})
            print('Answer: ' + result['answer'] + '\n')
            chat_history.append((query, result['answer']))

if __name__ == "__main__":
    model()
