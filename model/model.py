import sys
import json
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceHub

with open('./transcriber/transcriptions.json', 'r') as json_file:
    data = json.load(json_file)

repo_id = "mistralai/Mistral-7B-v0.1"
llm = HuggingFaceHub(huggingfacehub_api_token='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', repo_id=repo_id, model_kwargs={"temperature": 0.3, "max_new_tokens": 100})

for text in data:
    embeddings = HuggingFaceEmbeddings()

    db = Chroma.from_texts(text, embeddings)
    retriever = db.as_retriever(search_kwargs={'k': 2})

    qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever, return_source_documents=True)

    chat_history = []
    while True:
        query = input('Prompt: ')
        # To exit: use 'exit', 'quit', 'q', or Ctrl-D."
        if query.lower() in ["exit", "quit", "q"]:
            print('Exiting')
            sys.exit()
        result = qa_chain({'question': query, 'chat_history': chat_history})
        print('Answer: ' + result['answer'] + '\n')
        chat_history.append((query, result['answer']))
