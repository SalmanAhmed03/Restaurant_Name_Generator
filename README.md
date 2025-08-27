# 🍽️ Restaurant Name Generator

A fun and practical **Streamlit web app** powered by **LangChain** and **OpenAI** that generates:
- Catchy **restaurant names** (brandable, short, creative)
- Suggested **menu items** for each name

Built with:
- [Streamlit](https://streamlit.io/) for the UI  
- [LangChain](https://www.langchain.com/) for LLM orchestration  
- [OpenAI GPT models](https://platform.openai.com/) for text generation  

---

## ✨ Features
- Generate multiple **restaurant name ideas** by cuisine & tone.
- Instantly suggest **menu items** for each restaurant.
- Simple, interactive web interface.
- Easy to extend with new prompts.

---

## 🗂 Project Structure
```
Practice Project/
│
├── app.py        # Streamlit UI
├── ai.py         # Prompt templates + LangChain chains
├── llm.py        # LLM initialization (OpenAI client)
├── .venv/        # Virtual environment (local only)
└── README.md     # Documentation (this file)
```

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/your-username/restaurant-name-generator.git
cd restaurant-name-generator
```

### 2. Create virtual environment & install dependencies
```bash
python -m venv .venv
.venv\Scripts\activate   # On Windows
pip install -r requirements.txt
```

*(Create `requirements.txt` with these inside:)*

```
streamlit>=1.36.0
langchain>=0.2.14
langchain-openai>=0.1.7
openai>=1.40.0
python-dotenv>=1.0.1
```

### 3. Set your OpenAI API key
Currently, the project uses a **hard-coded key** for simplicity (in `llm.py`):

```python
# llm.py
OPENAI_API_KEY = "sk-proj-REPLACE_ME"
```

➡️ Replace `"sk-proj-REPLACE_ME"` with your actual API key from [OpenAI](https://platform.openai.com/account/api-keys).  

⚠️ **Never commit your real key** to GitHub. For production, move to environment variables instead.

### 4. Run the Streamlit app
```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🎮 Usage
- Select a **cuisine** (Pakistani, Italian, Japanese, etc.).
- Pick a **tone/vibe** (Modern, Rustic, Luxury, etc.).
- Choose how many **names** and **menu items** you want.
- Click **Generate** → get instant restaurant names + menus!

---

## ⚠️ Notes & Future Improvements
- **Hard-coded API key** in `llm.py` is for local dev only.  
  - Future: move to `.env` file or PyCharm Run Config for security.
- Add export options (CSV, PDF) for generated names & menus.
- Add “Regenerate” button for specific results.
- Support multiple LLM providers (OpenAI, Anthropic, Groq).

---

## 🛡 Security
- Do not commit your real OpenAI API key.
- If the key is ever exposed, rotate it immediately in your [OpenAI Dashboard](https://platform.openai.com/account/api-keys).

---

## 👨‍💻 Author
Developed by **[Salman Abbasi]**  
🎯 AI + Streamlit + LangChain experiment project.
