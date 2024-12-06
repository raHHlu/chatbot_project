from predict import predict_intent, get_response

print("Chatbot is ready! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    intents = predict_intent(user_input)
    response = get_response(intents)
    print(f"Chatbot: {response}")
