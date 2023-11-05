# Importing libraries
import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

# Dataset import here
dataset = pd.read_json('./transcriber/transcriptions.json')
transcripts = dataset['transcript']

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

corpus = []
for transcript in transcripts:
    # Lowercase the text
    review = transcript.lower()
    
    # Remove non-alphanumeric characters and extra whitespaces
    review = re.sub(r'[^a-zA-Z\s]', '', review)
    
    # Tokenize the text into words
    words = review.split()
    
    # Lemmatize each word
    words = [lemmatizer.lemmatize(word) for word in words]
    
    # Remove stopwords
    words = [word for word in words if word not in stopwords.words('english')]
    
    # Join the words back into a clean sentence
    clean_text = ' '.join(words)
    
    corpus.append(clean_text)

print(corpus)
