# 🤖 Gen AI Projects

> Hands-on Gen AI projects covering LLMs, Chatmodels, Embedding Models and Prompt Engineering using LangChain, HuggingFace, OpenAI, Anthropic, Google and Streamlit.

---

## 📁 Project Structure

gen-ai-projects/
│
├── 1.LLMS/
│   └── llm_demo.py              # LLM basics using HuggingFace
│
├── 2.Chatmodels/
│   ├── 1_chatmodel_openai.py    # OpenAI Chat Model
│   ├── 2_chatmodel_anthro.py    # Anthropic Claude Chat Model
│   ├── 3_chatmodel_google.py    # Google Gemini Chat Model
│   └── 4_chatmodel_hf_api.py   # HuggingFace Chat Model ✅ (Free & Working)
│
├── 3.Embeddedmodels/
│   ├── embedding_hf_local.py    # HuggingFace Local Embeddings
│   ├── openai_docs.py           # OpenAI Embeddings on Docs
│   └── openai.py                # OpenAI Embeddings
│
├── prompt_ui.py                 # Streamlit Prompt UI App
├── requirements.txt             # Dependencies
├── .env.example                 # Environment variables template
└── README.md                    # Project documentation

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🦜 LangChain | LLM framework |
| 🤗 HuggingFace | Free LLMs and Embeddings |
| 🟢 OpenAI | GPT Chat Models |
| 🟣 Anthropic | Claude Chat Models |
| 🔵 Google | Gemini Chat Models |
| 🎈 Streamlit | UI for Prompt App |
| 🐍 Python | Core Language |

---

## ✅ Working Projects (Free - No Paid API Needed)

| File | Description | Status |
|---|---|---|
| `llm_demo.py` | HuggingFace LLM demo | ✅ Working |
| `4_chatmodel_hf_api.py` | HuggingFace Chat Model | ✅ Working |
| `embedding_hf_local.py` | Local Embeddings | ✅ Working |
| `prompt_ui.py` | Streamlit App | ✅ Working |

## 🟡 Ready (Requires Paid API Key)

| File | Description | Status |
|---|---|---|
| `1_chatmodel_openai.py` | OpenAI GPT Model | 🔑 Needs API Key |
| `2_chatmodel_anthro.py` | Anthropic Claude | 🔑 Needs API Key |
| `3_chatmodel_google.py` | Google Gemini | 🔑 Needs API Key |

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

### 5. Run Streamlit App
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
- ✅ How to build a Streamlit UI with dynamic prompts
- ✅ Prompt Engineering basics — static vs dynamic prompts

---

## 👨‍💻 Author

**Ashish Chaubey**
- GitHub — https://github.com/AshishChaubey2003

---

## 📌 Note

> This is a learning project built while exploring the Gen AI ecosystem.
> All code is written from scratch as part of my AI learning journey. 🚀
