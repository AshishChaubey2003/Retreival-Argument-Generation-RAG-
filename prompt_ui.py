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

# dynamic
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.load import loads
from dotenv import load_dotenv
import streamlit as st
import json

load_dotenv()

# Model
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="conversational"
)
model = ChatHuggingFace(llm=llm)

# JSON se prompt load karo
with open("prompt_template.json", "r") as f:
    prompt = loads(json.dumps(json.load(f)))

chain = prompt | model

# UI
st.header('💼 Job & Career Assistant')
st.subheader('Your Personal AI Career Counselor')

job_role          = st.text_input('👔 Enter Job Role', placeholder="e.g. Data Scientist, Software Engineer")
job_domain        = st.text_input('🏢 Enter Domain', placeholder="e.g. IT, Finance, Marketing")
user_level        = st.selectbox('🎓 Your Experience Level', ['Fresher', 'Junior (1-3 years)', 'Mid Level (3-5 years)', 'Senior (5+ years)'])
response_language = st.selectbox('🌐 Response Language', ['English', 'Hindi', 'French', 'Spanish'])
response_tone     = st.selectbox('🎨 Tone of Response', ['formal', 'simple and friendly', 'motivational'])
word_limit        = st.slider('📝 Word Limit', min_value=200, max_value=1500, step=100, value=500)

if st.button('🚀 Get Career Advice'):
    if job_role.strip() and job_domain.strip():
        with st.spinner('Preparing your career advice...'):
            result = chain.invoke({
                "job_role": job_role,
                "job_domain": job_domain,
                "user_level": user_level,
                "response_language": response_language,
                "response_tone": response_tone,
                "word_limit": word_limit
            })
        st.success("✅ Here is your Career Advice!")
        st.write(result.content)
    else:
        st.warning("⚠️ Please enter Job Role and Domain before clicking.")