# AmbedkarGPT-Intern-Task

Project Overview

This is a command-line Question & Answer system that answers questions about a speech by Dr. B.R. Ambedkar.  
You type your question, and the program finds the answer using only the speech text, not the internet.

The system uses free and open-source tools:
LangChain: Connects all the parts together.
ChromaDB: Remembers and searches the speech efficiently.
HuggingFaceEmbeddings: Helps the computer understand sentences.
Ollama with Mistral 7B: Answers questions using a smart language model on your computer.

Everything runs entirely on your computer, does not need an internet connection, and does not require any paid services or accounts.  
This makes it safe, private, and free for anyone to use.

Setup Instructions
Install Ollama:

Download/install from ollama.com

Run ollama pull mistral to get the model locally.

Install Python packages:

Create a virtual environment:
python3 -m venv venv && source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run the Q&A System:

Place speech.txt in the root directory.

Launch:
python main.py

Usage
Enter user questions at the prompt. Answers will be generated from the speech content.

Type exit to quit.

Troubleshooting
Ensure Ollama daemon is running (ollama serve if not started automatically).

If dependencies fail, reinstall via pip install --upgrade -r requirements.txt.
