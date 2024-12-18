def chatbot():
    print("CodSoftBot: Hi! I am CodSoftBot. Type 'exit' to end the chat.")
while True:
  user_input = input("You: ")
  if user_input == "exit":
    print("CodSoftBot: bye! Have a nice day!")
    break
  else:
    print("CodSoftBot: Hi! I am CodSoftBot. Type 'exit' to end the chat.")


chatbot()
