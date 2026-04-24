from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# ✅ Hugging Face LLM
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="conversational",
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

# 🔹 Pydantic Model
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description="Give the sentiment of the feedback"
    )

parser2 = PydanticOutputParser(pydantic_object=Feedback)

# 🔹 Prompt 1 (Classifier)
prompt1 = PromptTemplate(
    template="""
Classify the sentiment of the following feedback text into positive or negative.

{feedback}

{format_instruction}
""",
    input_variables=["feedback"],
    partial_variables={
        "format_instruction": parser2.get_format_instructions()
    },
)

classifier_chain = prompt1 | model | parser2

# 🔹 Positive Response
prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback:\n{feedback}",
    input_variables=["feedback"],
)

# 🔹 Negative Response
prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback:\n{feedback}",
    input_variables=["feedback"],
)

# 🔹 Conditional Branch
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not determine sentiment"),
)

# 🔹 Final Chain
chain = classifier_chain | branch_chain

# 🔥 Run
output = chain.invoke({
    "feedback": "This is a terrible phone"
})

print("\n===== OUTPUT =====\n")
print(output)

# 🔹 Graph
try:
    chain.get_graph().print_ascii()
except:
    print("\nInstall: python -m pip install grandalf")