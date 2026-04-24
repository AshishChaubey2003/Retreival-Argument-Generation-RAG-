from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel
import json

# Load env variables
load_dotenv()

# 🔥 LLM Setup
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation",
    temperature=0.2
)

model = ChatHuggingFace(llm=llm)

# ✅ Step 1: TypedDict (LLM structured output)
class ReviewSchema(TypedDict):
    key_themes: Annotated[list[str], "Write key themes from the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["positive", "negative", "neutral"], "Return sentiment"]
    pros: Annotated[Optional[list[str]], "List of pros"]
    cons: Annotated[Optional[list[str]], "List of cons"]
    name: Annotated[Optional[str], "Name of the reviewer if mentioned"]

# Structured model
structured_model = model.with_structured_output(ReviewSchema)

# ✅ Step 2: Pydantic model (Validation)
class ReviewModel(BaseModel):
    key_themes: list[str]
    summary: str
    sentiment: Literal["positive", "negative", "neutral"]
    pros: Optional[list[str]] = None
    cons: Optional[list[str]] = None
    name: Optional[str] = None

    class Config:
        extra = "forbid"   # ❌ extra fields reject

# ✅ Input (Better prompt)
text = """
Analyze the following review and return structured data.

Return:
- key themes (list)
- summary
- sentiment (positive, negative, neutral)
- pros
- cons
- reviewer name (if any)

Review:
The iPhone 15 is an absolute beast in performance and camera quality. Dynamic Island is genuinely useful, not just a gimmick. Battery life has improved significantly. USB-C switch was long overdue but finally makes it universally convenient. Build quality feels premium with the titanium frame. However, the base storage of 128GB feels limiting at this price point. Price is also on the higher side for Indian consumers. Overall, best iPhone Apple has made — worth every rupee for power users!
"""

# ✅ Step 3: LLM Output
raw_result = structured_model.invoke(text)

print("\n🔹 Raw Output:")
print(raw_result)

# ✅ Step 4: Validation
try:
    validated_result = ReviewModel(**raw_result)

    print("\n✅ Validated Output:")
    print(validated_result)

    print("\n📦 JSON Output:")
    print(json.dumps(validated_result.model_dump(), indent=2))

    print("\n👤 Reviewer Name:")
    print(validated_result.name)

except Exception as e:
    print("\n❌ Validation Error:")
    print(e)