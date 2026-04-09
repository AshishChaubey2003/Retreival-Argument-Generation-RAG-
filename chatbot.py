from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import streamlit as st
import json
import os
from datetime import datetime

load_dotenv()

# ✅ Page Config
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ✅ CSS
st.markdown("""
    <style>
    .main { background-color: #f5f7fb; }
    section[data-testid="stSidebar"] { background-color: #1a1a2e; color: white; }
    section[data-testid="stSidebar"] * { color: white !important; }
    section[data-testid="stSidebar"] .stButton button {
        background-color: #00d4ff; color: black !important;
        font-weight: bold; border-radius: 20px; width: 100%;
        border: none; padding: 8px; margin: 3px 0;
    }
    section[data-testid="stSidebar"] .stButton button:hover {
        background-color: #0099bb; transition: 0.3s;
    }
    .stChatMessage {
        border-radius: 15px; padding: 12px; margin: 8px 0;
        background-color: #ffffff; box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    }
    .stChatMessage p { color: #1a1a2e !important; font-size: 15px; }
    div[data-testid="stChatInput"] {
        background-color: #ffffff; border-radius: 25px;
        border: 2px solid #00d4ff; padding: 5px 10px;
        box-shadow: 0px 2px 10px rgba(0,212,255,0.2);
    }
    div[data-testid="stChatInput"] textarea {
        background-color: #ffffff !important;
        color: #1a1a2e !important; font-size: 15px; border: none !important;
    }
    div[data-testid="stChatInput"] textarea::placeholder { color: #aaaaaa !important; }
    div[data-testid="stMetric"] {
        background-color: #ffffff; border-radius: 10px;
        padding: 10px; box-shadow: 0px 2px 6px rgba(0,0,0,0.1); margin: 5px 0;
    }
    div[data-testid="stMetric"] label { color: #aaaaaa !important; font-size: 13px; }
    div[data-testid="stMetric"] div { color: #00d4ff !important; font-size: 24px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# ✅ Chat History File
HISTORY_FILE = "chat_history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

# ✅ Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "saved_history" not in st.session_state:
    st.session_state.saved_history = load_history()
if "total_messages" not in st.session_state:
    st.session_state.total_messages = 0

# ✅ Model Load
@st.cache_resource
def load_model():
    llm = HuggingFaceEndpoint(
        repo_id="Qwen/Qwen2.5-72B-Instruct",
        task="conversational"
    )
    return ChatHuggingFace(llm=llm)

model = load_model()

# ✅ Sidebar
with st.sidebar:
    st.markdown("## 🤖 AI Chatbot")
    st.caption("Powered by Qwen 2.5 72B")
    st.divider()

    # Model Info
    st.markdown("### 🧠 Model")
    st.info("Qwen 2.5 72B Instruct")

    st.divider()

    # Stats
    st.markdown("### 📊 Chat Stats")
    st.metric("Total Messages", st.session_state.total_messages)
    st.metric("Current Session", len(st.session_state.chat_history))

    st.divider()

    # Buttons
    st.markdown("### 🗂️ Actions")
    if st.button("💾 Save Chat"):
        if st.session_state.chat_history:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            chat_data = {
                "timestamp": timestamp,
                "messages": [
                    {
                        "role": "user" if isinstance(m, HumanMessage) else "ai",
                        "content": m.content
                    }
                    for m in st.session_state.chat_history
                ]
            }
            st.session_state.saved_history.append(chat_data)
            save_history(st.session_state.saved_history)
            st.success("✅ Chat Saved!")
        else:
            st.warning("⚠️ No chat to save!")

    if st.button("🗑️ Clear Current Chat"):
        st.session_state.chat_history = []
        st.rerun()

    if st.button("🗑️ Clear All History"):
        st.session_state.saved_history = []
        save_history([])
        st.success("✅ Cleared!")

    # Saved Chats
    if st.session_state.saved_history:
        st.divider()
        st.markdown("### 📜 Saved Chats")
        for chat in reversed(st.session_state.saved_history):
            with st.expander(f"💬 {chat['timestamp']}"):
                for msg in chat["messages"]:
                    icon = "👤" if msg["role"] == "user" else "🤖"
                    st.write(f"{icon} {msg['content']}")

# ✅ Main UI
st.markdown("<h1 style='text-align:center; color:#00d4ff;'>🤖 AI Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Powered by HuggingFace + LangChain | Qwen 2.5 72B</p>", unsafe_allow_html=True)
st.divider()

# ✅ Display Chat
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user", avatar="👤"):
            st.write(message.content)
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.write(message.content)

# ✅ Chat Input
user_input = st.chat_input("💬 Type your message here...")

if user_input:
    with st.chat_message("user", avatar="👤"):
        st.write(user_input)

    st.session_state.chat_history.append(HumanMessage(content=user_input))

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("🤔 Thinking..."):
            result = model.invoke(st.session_state.chat_history)
            st.write(result.content)

    st.session_state.chat_history.append(AIMessage(content=result.content))
    st.session_state.total_messages += 1