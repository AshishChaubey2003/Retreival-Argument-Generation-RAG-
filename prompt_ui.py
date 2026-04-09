# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# import streamlit as st

# load_dotenv()

# # Initialize the model
# llm = HuggingFaceEndpoint(
#     repo_id="Qwen/Qwen2.5-72B-Instruct",
#     task="conversational"
# )

# model = ChatHuggingFace(llm=llm)

# st.header('Research Tool')

# user_input = st.text_input('Enter your prompt')

# if st.button('Summarize'):
#     if user_input.strip():
#         result = model.invoke(user_input)
#         st.write(result.content)
#     else:
#         st.warning("Please enter a prompt before clicking Summarize.")


# dynamics prompt
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Initialize the model
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="conversational"
)

model = ChatHuggingFace(llm=llm)

# Dynamic Prompt Template — 5+ line dynamic human message
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research assistant with deep knowledge across all domains. "
               "Your job is to provide well-structured, accurate and insightful research summaries."),
    ("human", """
    I am a {user_level} student researching about the topic: {user_topic}.
    
    Please help me with the following in {response_language} language:
    1. Give a brief introduction about {user_topic} in simple words.
    2. List the top 5 key points about {user_topic} that I must know.
    3. Explain how {user_topic} is used in real life with 2 practical examples.
    4. Mention any recent developments or trends related to {user_topic}.
    5. Suggest 3 resources (books, websites, or courses) where I can learn more about {user_topic}.
    
    Keep the tone {response_tone} and the total response within {word_limit} words.
    """)
])

chain = prompt | model

st.header('🔬 Research Tool')

# Dynamic inputs from user
user_topic    = st.text_input('📌 Enter your research topic')
user_level    = st.selectbox('🎓 Your academic level', ['Beginner', 'Intermediate', 'Advanced'])
response_language = st.selectbox('🌐 Response Language', ['English', 'Hindi', 'French', 'Spanish'])
response_tone = st.selectbox('🎨 Tone of Response', ['formal', 'simple and friendly', 'technical'])
word_limit    = st.slider('📝 Word Limit', min_value=100, max_value=1000, step=100, value=300)

if st.button('Summarize'):
    if user_topic.strip():
        result = chain.invoke({
            "user_topic": user_topic,
            "user_level": user_level,
            "response_language": response_language,
            "response_tone": response_tone,
            "word_limit": word_limit
        })
        st.write(result.content)
    else:
        st.warning("⚠️ Please enter a research topic before clicking Summarize.")