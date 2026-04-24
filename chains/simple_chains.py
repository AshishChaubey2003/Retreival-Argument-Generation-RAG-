from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template="generate five interesting facts about {topic}",
    input_variables=["topic"],
)

# Step 1: Create LLM
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="conversational",   
)

# Step 2: Wrap inside Chat model
model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

chain = prompt | model | parser

output = chain.invoke({"topic": "space exploration"})
print(output)
chain.get_graph().print_ascii()