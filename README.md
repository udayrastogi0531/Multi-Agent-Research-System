<div align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Robot.png" alt="Robot Emoji" width="80" />
  <h1>🚀 Multi-Agent Research System</h1>
  <p><i>An intelligent, multi-agent AI research assistant powered by Groq, LangChain, and Streamlit.</i></p>

  [![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
  [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
  [![LangChain](https://img.shields.io/badge/LangChain-1C3C3C.svg?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com/)
  [![Groq](https://img.shields.io/badge/Groq-Fast_AI-f55036.svg?style=for-the-badge)](https://groq.com)
</div>

---

## 🌟 Overview
**ResearchMind** utilizes the power of specialized AI agents working collaboratively to automate deep research. Enter any topic, and watch as our agents search the web, scrape deep content, draft comprehensive reports, and critically review them entirely autonomously!

## ⚙️ Architecture & Flow Diagram

The system employs a 4-stage pipeline passing critical state data to ensure the highest research quality.

```mermaid
graph TD
    classDef default fill:#0a0a0f,stroke:#ff8c32,stroke-width:2px,color:#f0ebe0;
    classDef highlight fill:#ff8c32,stroke:#ff8c32,stroke-width:2px,color:#0a0a0f,font-weight:bold;
    
    A[👤 User Input Topic]:::highlight --> B(💻 Streamlit UI)
    B --> C{🔍 Search Agent}
    C -->|Queries Tavily API| D[🌐 Top URLs & Snippets Fetch]
    D --> E{📄 Reader Agent}
    E -->|Selects Best URL & Scrapes| F[📝 Clean Scraped Content]
    F --> G{✍️ Writer Chain}
    G -->|Synthesizes Data| H[📄 Draft Research Report]
    H --> I{🧐 Critic Chain}
    I -->|Evaluates & Scores| J[✅ Final Report + Feedback UI]:::highlight
    J --> B
```

## ✨ Agent Roles
- **🔍 Search Agent:** Autonomously scours the web for the latest, most reliable information using the Tavily API.
- **📄 Reader Agent:** Deep-dives into the most relevant URLs, accurately scraping and cleaning text content.
- **✍️ Writer Chain:** Synthesizes the gathered intelligence into a beautifully structured Markdown report.
- **🧐 Critic Chain:** Acts as a strict quality-control reviewer, scoring the draft and suggesting areas to improve.

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/udayrastogi0531/Multi-Agent-Research-System.git
cd Multi-Agent-Research-System
```

### 2. Install dependencies
Ensure you have Python 3.9+ installed.
```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables
Create a `.env` file in the root directory and add your API keys:
```env
GROQ_API_KEY="your_groq_api_key_here"
TAVILY_API_KEY="your_tavily_api_key_here"
Demo https://multi-agent-research-system-o7ul.onrender.com/
```
*(Get your Groq API key from [GroqCloud](https://console.groq.com) and Tavily API key from [Tavily](https://tavily.com))*

### 4. Run the App
```bash
streamlit run app.py
```

---
<div align="center">
  <i>Built with ❤️ by Uday Rastogi</i>
</div>
  live https://multi-agent-research-system-ddk3knbpwwjz6nagswcati.streamlit.app/
  https://multi-agent-research-system-o7ul.onrender.com/
