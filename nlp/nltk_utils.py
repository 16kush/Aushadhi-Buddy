import numpy as np
from nltk.stem.porter import PorterStemmer

# Initialize the PorterStemmer from the NLTK library for word stemming.
stemmer = PorterStemmer()

# Function to convert a tokenized sentence into a bag of words representation.
def bag_of_words(tokenized_sentence, all_words):
    # Perform stemming on each word in the tokenized sentence and convert to lowercase.
    tokenized_sentence = [stemmer.stem(w.lower()) for w in tokenized_sentence]
    
    # Create a numpy array to represent the bag of words.
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        # Set the corresponding index in the bag array to 1.0 if the word exists in the tokenized sentence.
        if w in tokenized_sentence:
            bag[idx] = 1.0
    
    return bag 
