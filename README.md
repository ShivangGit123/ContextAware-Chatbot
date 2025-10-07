# 🧠 Context-Aware Chatbot

A conversational AI chatbot built with **LangChain**, **Groq/OpenAI LLMs**, and **Streamlit**, capable of maintaining **chat history and contextual memory** across sessions.  
It remembers previous messages, enabling smooth, human-like conversations with improved context understanding.

---

## 🚀 Features

- 💬 **Context Retention** — Remembers previous user queries within a session.  
- ⚙️ **LangChain Integration** — Manages prompt templates, chat memory, and LLM pipelines.  
- ⚡ **Groq / OpenAI API** — Fast and intelligent natural language generation.  
- 🧩 **Streamlit UI** — Interactive and responsive chat interface.  
- 📁 **Session Memory** — Keeps track of multi-turn dialogues.  

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend / UI** | Streamlit |
| **LLM Engine** | Groq API / OpenAI GPT |
| **Framework** | LangChain |
| **Memory** | ConversationBufferMemory / ChatMessageHistory |
| **Language** | Python |

---

## 🗂️ Project Structure

📁 context-aware-chatbot/
│
├── app.py # Main Streamlit application
├── requirements.txt # Dependencies
├── README.md # Project documentation

---

## ⚙️ Installation & Setup

1. **Clone the Repository**
   git clone https://github.com/ShivangGit123/ContextAware-Chatbot.git
   cd ContextAware-Chatbot

2. Create Virtual Environment
  python -m venv venv
  source venv/bin/activate   # On macOS/Linux
  venv\Scripts\activate      # On Windows

3. Install Dependencies

   pip install -r requirements.txt

 4. Set API Keys
  Create a .env file and add your API key:
  
  GROQ_API_KEY=your_api_key_here
  OPENAI_API_KEY=your_api_key_here   

  5. Run the App

  streamlit run app.py
 
   

