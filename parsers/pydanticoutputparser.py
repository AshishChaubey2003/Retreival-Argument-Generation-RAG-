from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str
    age: int
    city: str
parser = PydanticOutputParser(pydantic_object=Person)
template = PromptTemplate(
    template="""
Give me the details of a person.
{format_instructions}
""",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
chain = template | model | parser
output = chain.invoke({})
print(output)


    