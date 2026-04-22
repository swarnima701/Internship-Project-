import json
import random
import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer (first time only)
nltk.download('punkt')

# Load intents file
with open('intents.json') as file:
    data = json.load(file)

# Function to clean and tokenize input
def preprocess(text):
    return word_tokenize(text.lower())

# Function to find best response
def get_response(user_input):
    user_words = preprocess(user_input)

    for intent in data['intents']:
        for pattern in intent['patterns']:
            pattern_words = preprocess(pattern)

            # Check if any word matches
            if any(word in user_words for word in pattern_words):
                return random.choice(intent['responses'])

    return "Sorry, I didn't understand that. Can you rephrase?"

# Chat loop
print("🤖 Customer Service Chatbot (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = get_response(user_input)
    print("Bot:", response)