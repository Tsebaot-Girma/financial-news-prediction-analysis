# text_processing.py

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Download NLTK resources if not already present
nltk.download('punkt')
nltk.download('stopwords')

# Define stopwords
stop_words = set(stopwords.words('english'))

# Function to process headlines
def process_headlines(headlines):
    tokens = []
    for headline in headlines:
        words = word_tokenize(headline.lower())  # Tokenize and convert to lower case
        filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
        tokens.extend(filtered_words)
    return tokens

# Function to count the frequency of each token
def count_tokens(tokens):
    return Counter(tokens)
