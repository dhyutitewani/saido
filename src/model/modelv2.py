import sys
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceHub
import json

def initialize_qa_chain(data):
    repo_id = "mistralai/Mistral-7B-v0.1"
    llm = HuggingFaceHub(huggingfacehub_api_token='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', repo_id=repo_id, model_kwargs={"temperature": 0.4, "max_new_tokens": 100})
    embeddings = HuggingFaceEmbeddings()
    texts = [entry["transcript"] for entry in data]  # Extract the transcript data
    texts = [text.replace("\n", " ") for text in texts]  # Replace newlines with spaces
    db = Chroma.from_texts(texts, embeddings)
    retriever = db.as_retriever(search_kwargs={'k': 2})
    return ConversationalRetrievalChain.from_llm(llm, retriever, return_source_documents=True)

def ask_question(qa_chain, chat_history, query):
    result = qa_chain({'question': query, 'chat_history': chat_history})

    answer = result['answer'].split('\n\nQuestion:')[0].strip()
    indexH = answer.find("\n\nHelpful Answer:")
    # indexC = answer.find("\n\nCorrect Answer:")
    # indexR = answer.find("\n\nRelated Questions")
    # indexHash = answer.find("#")

    # print(result)
    # if indexHash != -1:
    #     answer = answer[:indexHash+1].strip()

    # if indexC != -1:
    #     answer = answer[:indexC].strip()

    # if indexR != -1:
    #     answer = answer[:indexR].strip()
    
    answer = answer[:indexH].strip()

    chat_history.append((query, result['answer']))
    return answer

if __name__ == "__main__":
    with open('/home/exvynai/code/dev/saido/src/model/transcriptions.json', 'r') as json_file:
        data = json.load(json_file)
    
    qa_chain = initialize_qa_chain(data)
    chat_history = []

    while True:
        query = input('Prompt: ')
        if query.lower() in ["exit", "quit", "q"]:
            print('Exiting')
            sys.exit()
        answer = ask_question(qa_chain, chat_history, query)
        print('Answer: ' + answer + '\n')
