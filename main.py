
def chatbot():
    print("CodSoftBot: Hi! I am CodSoftBot. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ").lower()  

        
        if user_input in ["hi", "hello"]:
            print("CodSoftBot: Hello! How can I help you?")
        elif user_input == "what is your name?":
            print("CodSoftBot: I am CodSoftBot, your friendly assistant.")
        elif user_input == "exit":
            print("CodSoftBot: bye! Have a nice day!")
            break
        else:
            print("CodSoftBot: I'm sorry, I don't understand that.")

chatbot()