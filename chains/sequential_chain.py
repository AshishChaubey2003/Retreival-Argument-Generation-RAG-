from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

promt1 = PromptTemplate(
    template="generate a detailed report on {topic}",
    input_variables=["topic"],
)
promt2 = PromptTemplate(
    template="generate a summary of the following report {report}",
    input_variables=["report"],
)
model =ChatHuggingFace(
    
    llm=HuggingFaceEndpoint(
        repo_id="Qwen/Qwen2.5-72B-Instruct",
        task="conversational",   
    )
)
parser = StrOutputParser()
chain = promt1 | model | parser | promt2 | model | parser
print(chain.invoke({"topic": "space exploration"}))
chain.get_graph().print_ascii()

