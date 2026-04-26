# Simple Python Chatbot

This is a beginner-friendly Python chatbot project. The chatbot uses basic string matching to respond to user messages such as greetings, asking how it is, and saying goodbye.

## Features

- Responds to basic user inputs
- Uses `.lower()` for case-insensitive matching
- Runs continuously using a `while True` loop
- Exits when the user types `bye`
- Beginner-friendly Python logic

## Technologies Used

- Python 3

## How It Works

The program takes user input and passes it to the `chatbot()` function.  
The input is converted to lowercase using `.lower()` so the chatbot can understand words even if the user types uppercase or mixed-case text.

Example:

```python
if "hello" in user:
    return "hi!"
