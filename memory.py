from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import os

llm = ChatOpenAI(model="gpt-4", temperature=0.7,openai_api_key="your api key")

# Define Chat Prompt Template
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a helpful AI chatbot having a friendly conversation with the user."
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)

# Initialize Conversation Memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Create Chatbot Chain
conversation = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory
)

# Chatbot Loop
print("🤖 AI Chatbot: Hello! How can I help you today? (Type 'exit' to end)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("🤖 AI Chatbot: Goodbye! Have a great day!")
        break

    # Get AI response
    response = conversation({"question": user_input})["text"]

    # Display AI response
    print(f"🤖 AI Chatbot: {response}\n")