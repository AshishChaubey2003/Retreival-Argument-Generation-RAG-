from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(models_name= "sentence-transformers/all-MiniLM-L6-v2")

document =[
    "I love machine learning",
    "FastAPI is fast and easy",
    "Python is great for data science"
    
]
embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

result = embedding.embed_query(document)
print(str(result))