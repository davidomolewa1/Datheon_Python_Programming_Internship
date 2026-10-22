# TechStore Support Assistant 🤖

A lightweight, rule-based customer support simulation chatbot built with Python. This application parses user queries using regular expressions (`re`), maps them to distinct intents, and pulls responses from a decoupled dictionary-based knowledge base.

---

## 🚀 How to Run the Program

1. Ensure you have **Python 3.x** installed on your system.
2. Clone or download this project directory to your local machine.
3. Save the main source code as `chatbot.py`.
4. Open your terminal or command prompt, navigate to the directory containing the file, and run:
   ```bash
   python chatbot.py
   ```
5. Interact with the bot in real time. Type `exit`, `quit`, or `bye` to cleanly shut down the program.

---

## 🛠️ System Architecture

The chatbot relies on a deterministic processing pipeline:
1. **Input Normalisation:** Cleans raw user strings by stripping leading/trailing whitespace and converting characters to lowercase.
2. **Regex Intent Engine:** Evaluates the processed string against predefined word-boundary (`\b`) regex patterns to catch explicit variations (e.g., matching "open" while ignoring "openly").
3. **Decoupled Knowledge Base:** Maps the verified intent key directly to its response string in a separate dictionary schema, allowing seamless text updates without altering runtime code.

---

## ⚠️ Known Limitations (Rule-Based Constraints)

Unlike a modern Large Language Model (LLM) or generative AI, this assistant operates strictly on static rules. Users should be aware of the following technical constraints:

* **Strict Sequential Priority (Multi-Intent Blindness):** The bot uses an `if/elif/else` structure. If a user asks a complex question containing multiple valid keys—for example, *"Do you sell **laptops** and what are your **hours**?"*—the bot will only resolve the first matched conditional branch (`products`) and completely ignore subsequent questions.
* **No Contextual Memory:** The system evaluates every user submission independently. It does not remember the message before it, making deep follow-ups or multi-turn context impossible.
* **Typo Vulnerability:** The regular expression patterns rely on correct spelling or explicit variance mappings. Typographical errors outside the mapped regex bounds will automatically trigger the fallback default layer.