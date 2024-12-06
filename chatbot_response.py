from tensorflow.keras.models import load_model
import random

model = load_model('chatbot_model.h5')

def clean_input(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    return [lemmatizer.lemmatize(w.lower()) for w in sentence_words]

def predict_intent(sentence):
    bow = [1 if w in clean_input(sentence) else 0 for w in words]
    result = model.predict(np.array([bow]))[0]
    return [{"intent": classes[i], "probability": res} for i, res in enumerate(result) if res > 0.25]

def get_response(intent_list):
    for intent in data['intents']:
        # Change 'intent' to 'tag' to access the intent label
        if intent['tag'] == intent_list[0]['intent']:
            return random.choice(intent['responses'])

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    intents = predict_intent(user_input)
    print("Bot:", get_response(intents))
