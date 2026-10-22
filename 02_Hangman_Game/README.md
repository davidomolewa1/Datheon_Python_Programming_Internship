# Hangman Word Guessing Game🎮

A Python-based command-line Hangman game featuring a tricky duplicate reveal mechanic, smart guess history tracking, and visual ASCII art stages. 

Unlike traditional Hangman games that reveal all identical letters at once, this **Hard-Mode** version only reveals a *single random instance* of a duplicate letter per guess, requiring strategic thinking and repeated attempts from the player.

---

## ✨ Features

*   **🎲 Randomized Duplicate Reveal:** If a secret word contains duplicate letters (e.g., the 'l's in "hello"), guessing that letter will only open up *one* random position at a time.
*   **🧠 Smart History Tracking:** Prevents players from losing lives on repeated incorrect guesses, while allowing them to guess the same correct letter again if hidden duplicates still remain.
*   **🎨 Dynamic ASCII Art:** Features 7 visual evolution stages of the hangman gallows that update in real-time based on your remaining lives.
*   **💡 Expressive UI:** Clear, engaging terminal feedback enhanced with emojis for victories, losses, and match discoveries.

---

## 🛠️ How It Works (The Logic)

1.  **State Management:** The game initializes with `6` incorrect guess opportunities. 
2.  **Tracking Array:** The secret word is mapped to a mutable list of dashes `["-", "-", ...]`.
3.  **Filtered Scanning:** Using Python's `enumerate()`, the application filters inputs down to exact index matches that haven't been uncovered yet.
4.  **Random Selection:** If multiple hidden positions match the user's input, `random.choice()` picks a single target position to reveal.

---

## 🚀 Getting Started

### Prerequisites
*   Python 3.x installed on your machine.

### Installation & Execution
1. Clone or download this repository.
2. Open your terminal or command prompt in the project directory.
3. Run the script using:
   ```bash
   python hangman.py
   ```

---

## 🕹️ Gameplay Preview

```text
WELCOME TO HANGMAN WORD GUESSING GAME

       +---+

       |   |
           |
           |
           |
           |
     =========
    
HERE IS A HINT TO THE NUMBER OF WORDS 😉
- - - - -

Enter a letter: e
Good guess! 👍 A 'e' was revealed

       +---+

       |   |
           |
           |
           |
           |
     =========
    
🔄 Word progress:  - - - - e
📋 All guesses made:  e
```
