import re

# Function to match message itent
def match_intent(clean_input):
    # Redefining to use regular expression setting boundaries to ensure matching whole words only
    hours_pattern = r'\b(hours|open|close|time|timing|when)\b'
    return_pattern = r'\b(return|refund|exchange|policy)\b'
    product_pattern = r'\b(laptop|phone|tv|sell|buy|device|stock|android|apple|macbook|iphone)\b'
    support_pattern = r'\b(contact|support|help|call|email|agent|phone number)\b'

    # Using re.search to return a match object if found, or None if not found
    # Using re.IGNORECASE as an extra layer of safety
    if re.search(hours_pattern, clean_input, re.IGNORECASE):
        return "TechStore: We are open Monday to Friday from 9:00 AM to 6:00 PM, and Saturdays from 10:00 AM to 4:00 PM. We are closed on Sundays."
        
    elif re.search(return_pattern, clean_input, re.IGNORECASE):
        return "TechStore: You can return any item within 30 days of purchase for a full refund. Items must be in their original packaging."
        
    elif re.search(product_pattern, clean_input, re.IGNORECASE):
        return "TechStore: Yes, we sell a wide range of electronics including laptops, smartphones, and smart TVs! What specific device are you looking for?"
        
    elif re.search(support_pattern, clean_input, re.IGNORECASE):
        return "TechStore: You can reach our support team via email at support@techstore.com or call us at 1-800-555-TECH."
        
    else:
        # Fallback response if no keywords match
        return "TechStore: I'm not sure I quite understood that. You can ask me about our opening hours, return policy, products, or how to contact support."

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
            
        # Call keyword matching function and output response
        response = match_intent(clean_input)
        print(response)

# Run the chatbot
if __name__ == "__main__":
    start_chatbot()