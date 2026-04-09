from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
chatModel = ChatOpenAI(model="gpt-4", temperature=0.9, max_tokens=150)  # temperature is used to control the randomness of the output. Higher temperature means more random output, while lower temperature means more deterministic output. The default value is 0.7, but you can adjust it according to your needs.
result = chatModel.invoke("What is the capital of india?")
print(result.content) # agar content nahi aata to result print kar dena. content nahi aayega to pura result print hoga.

