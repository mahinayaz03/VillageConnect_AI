import re
from difflib import SequenceMatcher

# Common words that don’t carry meaning
stopwords = {
    "is", "the", "a", "an", "are", "what", "when",
    "how", "to", "for", "of", "in", "on", "at"
}

def preprocess(text):
    # Lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove stopwords
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords]
    
    return " ".join(filtered_words)

def calculate_similarity(input_text, stored_text):
    input_text = preprocess(input_text)
    stored_text = preprocess(stored_text)
    
    return SequenceMatcher(None, input_text, stored_text).ratio()