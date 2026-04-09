from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

documnets =[
    "I love machine learning",
    "FastAPI is fast and easy",
    "Python is great for data science"
]
result = embedding.embed_documents(documnets)
print(str(result))