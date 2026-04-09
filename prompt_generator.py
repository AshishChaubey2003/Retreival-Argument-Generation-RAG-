from langchain_core.prompts import ChatPromptTemplate
from langchain_core.load import dumps
import json

# Real World Job/Career Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert career counselor and HR professional with 15+ years of experience. "
               "You help job seekers with resume building, interview preparation, career guidance and job search strategies."),
    ("human", """
    I am a {user_level} professional looking for a job in {job_domain} domain.
    
    Please help me with the following in {response_language} language:
    1. What are the top 5 in-demand skills required for {job_role} in 2025?
    2. How should I prepare my resume for {job_role} position? Give 3 key tips.
    3. What are the most common interview questions asked for {job_role}? List top 5.
    4. What is the average salary range for {job_role} in India?
    5. Which top companies are hiring for {job_role} right now?
    6. Suggest a 30-day preparation roadmap for cracking {job_role} interview.
    
    Keep the tone {response_tone} and the total response within {word_limit} words.
    """)
])

# JSON mein save karo
with open("prompt_template.json", "w") as f:
    json.dump(json.loads(dumps(prompt)), f, indent=2)

print("✅ Job/Career Prompt saved as prompt_template.json")