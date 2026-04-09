from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

chatModel = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro-latest",   # 👈 pro ki jagah flash use karo (free)
    temperature=0.9
)

result = chatModel.invoke("What is the capital of India?")
print(result.content)