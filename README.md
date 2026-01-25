# 🤖 Agentic AI Chainlit Assistant

An **Agentic AI Assistant** built using **LlamaIndex**, **Chainlit**, and **Groq LLMs**, capable of reasoning step-by-step and using tools to solve problems.  
This project demonstrates modern **AI agent architecture (ReAct)** with a clean chat UI.

---

##  Features

-  **ReAct Agent (Reason + Act)**
-  Tool usage via Python functions
-  Interactive chat UI using Chainlit
-  Fast inference using Groq API
-  Async-first agent workflow (latest LlamaIndex)
-  Clean, modular, and extensible codebase

---

## 🏗️ Architecture Overview

User
│
▼
Chainlit UI (Async Chat)
│
▼
ReAct Agent (LlamaIndex)
│
├─ Reasoning (LLM)
├─ Tool Selection
├─ Tool Execution (Python Functions)
│
▼
Final Response → UI




    
    ---
    
    ##  Tech Stack
    
    | Technology | Purpose |
    |---------|--------|
    | **Python** | Core programming language |
    | **Chainlit** | Chat UI framework |
    | **LlamaIndex** | Agent framework |
    | **ReAct Agent** | Reasoning + tool execution |
    | **Groq API** | High-speed LLM inference |
    | **dotenv** | Environment variable management |
    
    ---

##  Project Structure

agentic-ai-chainlit-assistant/
│
├── app_chainlit.py # Main Chainlit application
├── requirements.txt # Python dependencies
├── chainlit.md # Chainlit UI config
├── .gitignore
└── README.md


---

## ⚙️ Setup Instructions

### 1️ Clone the Repository
    
    git clone https://github.com/sahilshore/Agentic-AI-Chainlit-Assistant.git
    cd Agentic-AI-Chainlit-Assistant

### 2️ Create Virtual Environment
python -m venv chain


Activate it:

Windows

    chain\Scripts\activate


Linux / macOS

source chain/bin/activate

### 3️ Install Dependencies
    pip install -r requirements.txt

### 4️ Set Environment Variables

Create a .env file in the root directory:

    GROQ_API_KEY=your_groq_api_key_here


(Optional but recommended)

    GROQ_MODEL=llama-3.1-8b-instant

5️ Run the Application 🚀

    chainlit run app_chainlit.py


Open your browser at:

    http://localhost:8000

💡 Example Usage

Try asking:

    (65 * 7) / 8


The agent will:

1. Reason about the problem

2. Select the correct tool

3. Execute it

4. Return the final answer

####  Key Concepts Demonstrated

**.** Agentic AI workflows

**.** Tool calling with structured functions

**.** Async execution with Chainlit

**.** Handling breaking changes in modern AI frameworks

**.** Real-world LLM provider integration

#### Notes

**.** No local ML models are required

**.** Groq API handles all inference

**.** Warnings about PyTorch / TensorFlow can be safely ignored

**.** Built using latest LlamaIndex APIs

#### Future Improvements

**.**Conversation memory

**.** Streaming responses

**.** Multi-agent system

**.** Custom tool visualisation

**.** FastAPI backend deployment
