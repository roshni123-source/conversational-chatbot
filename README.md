# AI Chatbot using LangChain and OpenAI GPT-4

This project is a simple AI chatbot built using LangChain and OpenAI's GPT-4 model. The chatbot maintains conversation history using memory and provides responses in a friendly conversational style.

## Features
- Utilizes OpenAI's GPT-4 for natural language processing.
- Uses LangChain's `LLMChain` for structured conversation flow.
- Maintains conversation history with `ConversationBufferMemory`.
- Interactive command-line interface.

Replace `openai_api_key` in the script with your OpenAI API key.

## Dependencies
Ensure you have the following dependencies installed:

```bash
pip install langchain langchain-openai
```

## Usage
Run the chatbot script with:
```bash
python memory.py
```
The chatbot will start an interactive session. Type your queries, and the AI will respond. Type `exit` to end the session.



