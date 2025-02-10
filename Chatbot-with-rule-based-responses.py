import re

def chatbot():
    print("Hello! I am your chatbot. Type 'exit' to end the conversation.")
    
    while True:
        # Take user input
        user_input = input("You: ").lower()

        # Check for exit condition
        if user_input == "exit":
            print("Goodbye!")
            break
        
        # Respond based on predefined rules
        if re.search(r"hello|hi|hey", user_input):
            print("Chatbot: Hello! How can I help you today?")
        elif re.search(r"how are you|how's it going", user_input):
            print("Chatbot: I'm just a program, but I'm doing fine! How about you?")
        elif re.search(r"your name", user_input):
            print("Chatbot: I am a chatbot without a name, but you can call me Chatbot!")
        elif re.search(r"bye|goodbye", user_input):
            print("Chatbot: Goodbye! Have a nice day!")
        elif re.search(r"help", user_input):
            print("Chatbot: Sure! I can assist you with greetings and general conversation.")
        else:
            print("Chatbot: Sorry, I don't understand that. Can you ask something else?")
            

# Run the chatbot
chatbot()
