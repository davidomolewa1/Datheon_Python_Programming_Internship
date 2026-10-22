# basic test
def start_chatbot():
    # Bot Welcome message
    print("Welcome to TechStore Support Assistant!")
    print("Type 'help' to see what I can do, or 'exit' to quit.\n")
    
    # Conversation loop
    while True:
        # Get input from the user
        user_input = input("You: ")
        
        # Normalise the input (change to lowercase and remove trailing/leading spaces)
        clean_input = user_input.strip().lower()
        
        # Check for clean exit commands
        if clean_input in ['bye', 'exit', 'quit']:
            print("TechStore: Thank you for visiting TechStore. Goodbye!")
            break
            
        # Temporary print statement to see user input
        print(f"TechStore: I received your message: '{user_input}'.")

# Run the chatbot
if __name__ == "__main__":
    start_chatbot()