# 🤖 Gen AI Projects

> Hands-on Gen AI projects covering LLMs, Chatmodels, Embedding Models, Prompt Engineering and AI Chatbot using LangChain, HuggingFace, OpenAI, Anthropic, Google and Streamlit.

---

## 📁 Project Structure
gen-ai-projects/
│
├── 1.LLMS/
│   └── llm_demo.py                 # LLM basics using HuggingFace
│
├── 2.Chatmodels/
│   ├── 1_chatmodel_openai.py       # OpenAI Chat Model
│   ├── 2_chatmodel_anthro.py       # Anthropic Claude Chat Model
│   ├── 3_chatmodel_google.py       # Google Gemini Chat Model
│   └── 4_chatmodel_hf_api.py      # HuggingFace Chat Model ✅ (Free & Working)
│
├── 3.Embeddedmodels/
│   ├── embedding_hf_local.py       # HuggingFace Local Embeddings
│   ├── openai_docs.py              # OpenAI Embeddings on Docs
│   └── openai.py                   # OpenAI Embeddings
│
├── chatbot.py                      # ✅ AI Chatbot with Streamlit UI
├── prompt_generator.py             # Dynamic Prompt Generator
├── prompt_template.json            # Saved Prompt Template
├── prompt_ui.py                    # Streamlit Prompt UI App
├── requirements.txt                # Dependencies
├── .env.example                    # Environment variables template
└── README.md                       # Project documentation

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🦜 LangChain | LLM framework |
| 🤗 HuggingFace | Free LLMs and Embeddings |
| 🟢 OpenAI | GPT Chat Models |
| 🟣 Anthropic | Claude Chat Models |
| 🔵 Google | Gemini Chat Models |
| 🎈 Streamlit | UI for Chatbot and Prompt App |
| 🐍 Python | Core Language |

---

## ✅ Working Projects (Free - No Paid API Needed)

| File | Description | Status |
|---|---|---|
| `llm_demo.py` | HuggingFace LLM demo | ✅ Working |
| `4_chatmodel_hf_api.py` | HuggingFace Chat Model | ✅ Working |
| `embedding_hf_local.py` | Local Embeddings | ✅ Working |
| `chatbot.py` | AI Chatbot with Streamlit UI | ✅ Working |
| `prompt_ui.py` | Dynamic Prompt Streamlit App | ✅ Working |

## 🟡 Ready (Requires Paid API Key)

| File | Description | Status |
|---|---|---|
| `1_chatmodel_openai.py` | OpenAI GPT Model | 🔑 Needs API Key |
| `2_chatmodel_anthro.py` | Anthropic Claude | 🔑 Needs API Key |
| `3_chatmodel_google.py` | Google Gemini | 🔑 Needs API Key |

---

## 🤖 AI Chatbot Features

| Feature | Details |
|---|---|
| 🧠 Model | Qwen 2.5 72B (HuggingFace) |
| 💬 Memory | Multi-turn conversation history |
| 💾 Save Chat | JSON mein save hoti hai history |
| 📊 Stats | Real-time message count |
| 🎨 UI | Custom dark sidebar + clean UI |
| 🗑️ Clear | Current ya full history clear |

---

## ⚙️ How to Run

### 1. Clone the repo
```bash
git clone https://github.com/AshishChaubey2003/gen-ai-projects.git
cd gen-ai-projects
```

### 2. Create virtual environment
```bash
python -m venv genenv
genenv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables
```bash
copy .env.example .env
# Add your API keys in .env file
```

### 5. Run AI Chatbot
```bash
streamlit run chatbot.py
```

### 6. Run Prompt UI App
```bash
streamlit run prompt_ui.py
```

---

## 🔑 Environment Variables

Create a `.env` file using `.env.example` as template:
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
GOOGLE_API_KEY=your_google_key_here
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here

Get your free HuggingFace token here — https://huggingface.co/settings/tokens

---

## 📚 What I Learned

- ✅ How to use LLMs with LangChain
- ✅ Difference between LLMs and Chat Models
- ✅ How to integrate OpenAI, Anthropic, Google and HuggingFace
- ✅ What are Embedding Models and how they work
- ✅ How to build a Streamlit Chatbot with conversation memory
- ✅ How to save and load chat history
- ✅ Prompt Engineering basics — static vs dynamic prompts
- ✅ How to build dynamic prompt UI with Streamlit

---

## 👨‍💻 Author

**Ashish Chaubey**
- GitHub — https://github.com/AshishChaubey2003

---

## 📌 Note

> This is a learning project built while exploring the Gen AI ecosystem.
> All code is written from scratch as part of my AI learning journey. 🚀
