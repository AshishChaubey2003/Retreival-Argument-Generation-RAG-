from langchain.runnable import huggingface_hub
from langchain_core.prompts import PromptTemplate
from langcjhain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import Runnablesequence

load_dotenv()

prompt = PromptTemplate(
    template="What year did the first   moon landing happen?",
    input_variables=[],     
)
llm = huggingface_hub.HuggingFaceEndpoint(
    repo_id="google/flan-t5-xxl",
    task="text2text-generation",
)
model = huggingface_hub.ChatHuggingFace(llm=llm)
parser = StrOutputParser()
chain = prompt | model | parser
runnable = Runnablesequence(
    steps=[chain]
)
if __name__ == "__main__":
    output = runnable.invoke({})
    print(output)

