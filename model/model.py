import spacy
import json
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the JSON data
with open('./transcriber/transcriptions.json', 'r') as file:
    data = json.load(file)

# Extract and clean the transcripts
transcripts = [entry['transcript'] for entry in data]

nltk.download('stopwords')

# Cleaning the text using provided code
corpus = []
for transcript in transcripts:
    review = re.sub('[^a-zA-Z]', ' ', transcript)
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)
    corpus.append(review)

# Process the cleaned text
cleaned_text = " ".join(corpus)

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Tokenize the text
doc = nlp(cleaned_text)

# Create a list of sentences
sentences = [sent.text for sent in doc.sents]

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)

# Maintain conversation history
conversation_history = []

# Define a function to answer questions
def answer_question(question):
    question = re.sub('[^a-zA-Z]', ' ', question)
    question = question.lower()

    # Calculate TF-IDF vectors for the question and the sentences
    tfidf_matrix_question = tfidf_vectorizer.transform([question])
    cosine_similarities = cosine_similarity(tfidf_matrix_question, tfidf_matrix)

    # Sort sentences by similarity to the question
    ranked_sentences = sorted(enumerate(cosine_similarities[0]), key=lambda x: x[1], reverse=True)

    # Extract the most similar sentence
    most_similar_sentence_index, similarity = ranked_sentences[0]

    # Return the most similar sentence as the answer
    answer = sentences[most_similar_sentence_index]

    # Add the user's question to the conversation history
    conversation_history.append(question)

    if similarity > 0.0:
        return answer
    else:
        return "I couldn't find an answer to your question."

# Example usage:
print("\n")
user_question1 = "What is Tails OS?"
print(user_question1,"\n")
response1 = answer_question(user_question1)
print(response1,"\n")

user_question2 = "Tell me more about its features."
print(user_question2,"\n")
response2 = answer_question(user_question2)
print(response2,"\n")

user_question3 = "How do I set it up?"
print(user_question3,"\n")
response3 = answer_question(user_question3)
print(response3,"\n")