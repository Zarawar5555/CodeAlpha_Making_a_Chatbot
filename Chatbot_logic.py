import json
import random

with open("intents.json") as file:
    data = json.load(file)

def get_response(msg):
    msg = msg.lower()
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern in msg:
                return random.choice(intent["responses"])
    return "I'm not sure how to answer that yet."
