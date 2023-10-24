import json
import random

from rasa_nlu.training_data import load_data
from rasa_nlu import config  
from rasa_nlu.model import Trainer

# Load video transcript JSON
with open('transcription.json') as f:
  data = json.load(f)

transcript = data['transcript']

# Extract Q&A pairs from transcript
sentences = transcript.split('.')
qa_pairs = []
for sentence in sentences:
  if '?' in sentence:
    question = sentence.strip()
    answer = find_answer(question, transcript)  
    qa_pairs.append((question, answer))

training_data = load_data(qa_pairs)  

trainer = Trainer(config.load("config.yml"))
model = trainer.train(training_data)

def find_answer(question, transcript):
  # Logic to find answer to question based on transcript
  return "Answer to: " + question 

def chat(question):
  response = model.parse(question)
  intent = response['intent']['name']

  if intent == 'ask_question':
    entities = response['entities']
    question = entities[0]['value']

    if question in [q[0] for q in qa_pairs]:
      return random.choice([a for q,a in qa_pairs if q==question])
    else:
      return "Sorry I don't know the answer to that based on the given transcript"

  else:
    return "I didn't understand your question"

print(chat("What is the Linux file system?"))