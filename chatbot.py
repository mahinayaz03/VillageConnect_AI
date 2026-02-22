import random
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load intents
with open("data.json") as file:
    data = json.load(file)

# Prepare training data
patterns = []
tags = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

def get_response(user_input):

    if not user_input:
        return "Please enter a valid question."

    user_input = user_input.lower()

    user_vector = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vector, X)

    max_score = similarity.max()
    index = similarity.argmax()
    tag = tags[index]

    # Confidence threshold
    if max_score < 0.4:
       return "Sorry, I didn't understand that. Please rephrase.", max_score

    for intent in data["intents"]:
        if intent["tag"] == tag:
           return random.choice(intent["responses"]), max_score

    return "Sorry, something went wrong.", max_score