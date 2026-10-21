import random as rand

# The 7 stages of ASCII art (from index 0 to 6)
# Position 0 means 6 tries left (empty gallows)
# Position 6 means 0 tries left (game over)
stages = [
    """
       +---+

       |   |
           |
           |
           |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |
           |
           |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |

       |   |
           |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |
      /|   |
           |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |
      /|\\  |
           |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |
      /|\\  |
      /    |
           |
     =========
    """,
    """
       +---+

       |   |
       O   |
      /|\\  |
      / \\  |
           |
     =========
    """
]

# Load secret english words from the text file
with open("google-10000-english-no-swears.txt", "r", encoding="utf-8") as f:
    eng_word = [line.strip() for line in f if line.strip()]

# Ramdomly select a secret word from the list
secret_word = rand.choice(eng_word).lower()

# List of dashes to represent the length of the secret word
hidden_list = ["-"] * len(secret_word)
guessed_letters = []

# Limit of incorrect attempts
incorrect_guess = 6 

# Welcome display notes
print("WELCOME TO HANGMAN WORD GUESSING GAME")
print(stages[0])
print("HERE IS A HINT TO THE NUMBER OF WORDS 😉")
print(" ".join(hidden_list))

# Keep the game running as long as they have tries left and the dashes are remaining
while incorrect_guess > 0 and "-" in hidden_list:
    # User input
    guess = input("\nEnter a letter: ").lower()
    
    # Handling multiple letter entries at once or not numeric value
    if len(guess) != 1 or not guess.isalpha():
        print("You can only enter a single letter 🙃")
        continue
    
    # Collect all valid hidden index positions for the input letter using a loop
    matching_indices = []
    for index, value in enumerate(secret_word):
        if value == guess and hidden_list[index] == "-":
            matching_indices.append(index)

    # History check to see if input word has been guessed before and no hidden copies left
    if guess in guessed_letters and not matching_indices:
        print(f"⏹️ You already fully tried '{guess}'! It is either wrong or completely revealed")
        print(f"📋 Letters tried so far {", ".join(guessed_letters)}")

    # Record the letter if it is the first time that they typed it
    if guess not in guessed_letters:
        guessed_letters.append(guess)

    # Game Logic
    if matching_indices:
        # pick a random position out of remaining duplicates
        chosen_index = rand.choice(matching_indices)
        hidden_list[chosen_index] = guess
        print(f"Good guess! 👍 A '{guess}' was revealed")
    else:
        # Penalty if word not in secret words or fully revealed
        incorrect_guess -= 1
        if incorrect_guess > 0:
            print(f"❌ Incorrect or already fully revealed! You have {incorrect_guess} guess left")
        else:
            print("You have zero tries left 🙅‍♂️")
    
    # Calculate which art phase to print
    current_stage_index = 6 - incorrect_guess
    print(stages[current_stage_index])

    # Show status updates to the players
    word_progress = " ".join(hidden_list)
    guesses_made = " ".join(guessed_letters)
    print("🔄 Word progress: ", word_progress)
    print("📋 All guesses made: ", guesses_made)

# Game result
if "-" not in hidden_list:
    print("\n🎉 You win! you revealed all the words correctly")
else:
    print(f"\n💀 You lose!, Game Over!.The secret word was: '{secret_word}'")