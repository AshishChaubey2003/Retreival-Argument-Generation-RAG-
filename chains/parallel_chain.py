from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

# ✅ Create base LLM
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="conversational",
)

# ✅ Wrap in Chat Model
model = ChatHuggingFace(llm=llm)

# Prompts
prompt1 = PromptTemplate(
    template="generate short and simple notes from the following {text}",
    input_variables=["text"],
)

prompt2 = PromptTemplate(
    template="generate five question answers from the following text {text}",
    input_variables=["text"],
)

prompt3 = PromptTemplate(
    template="merge the provided notes and quiz into a single response:\nNotes: {notes}\nQuiz: {quiz}",
    input_variables=["notes", "quiz"],
)

parser = StrOutputParser()

# Individual chains
chain1 = prompt1 | model | parser
chain2 = prompt2 | model | parser

# ✅ Parallel execution
parallel_chain = RunnableParallel(
    notes=chain1,
    quiz=chain2
)

# Final chain
final_chain = parallel_chain | prompt3 | model | parser

# Run
output = final_chain.invoke({
    "text": "Space exploration is the ongoing discovery and exploration of celestial structures in outer space..."
})

print(output)

# Graph (optional)
final_chain.get_graph().print_ascii()