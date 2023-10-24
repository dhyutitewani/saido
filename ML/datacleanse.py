# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Dataset import here
dataset = pd.read_json('./Dataset/transcriptions.json')
transcripts = dataset['transcript']

# Cleaning the text
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
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
print(corpus)