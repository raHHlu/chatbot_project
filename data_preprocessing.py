import nltk
from nltk.stem import WordNetLemmatizer
import json
import numpy as np

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')  # Download punkt_tab without 'tokenizers/' prefix

lemmatizer = WordNetLemmatizer()

# Load data
with open('intents.json') as file:
    data = json.load(file)

# Preprocessing
words, classes, documents = [], [], []
for intent in data['intents']:
    for pattern in intent['patterns']:
        tokens = nltk.word_tokenize(pattern)
        words.extend(tokens)
        # Use 'tag' instead of 'intent' to access the intent label
        documents.append((tokens, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = sorted(set(lemmatizer.lemmatize(w.lower()) for w in words if w not in ['?', '!']))
classes = sorted(classes)
