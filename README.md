# AI Research Agent

An autonomous AI-powered research assistant designed to gather, analyze, and summarize information from the web. The agent leverages **LangChain**, **LangGraph**, **Pydantic**, and **FireCrawl** along with **Large Language Models (LLMs)** to streamline the process of researching complex topics.

Useful for students, researchers, engineers, and analysts who want faster, structured research insights.

---

## 🚀 Features
- Automated Research - Searches the web and extracts relevant information
- LLM-Powered Summaries - Uses advanced prompt engineering to synthesize insights
- LangChain and LangGraph - Provides modular pipelines and graph-based orchestration of tasks
- Pydantic Models - Ensures data validation and structured inputs/outputs
- FireCrawl - Handles large-scale web crawling with structured extraction
- Extendable - Add tools, workflows, or specialized prompts for your domain
  
---

## ⚡Getting Started
1. Clone the repository
```bash
git clone https://github.com/sebcheung/AI-Research-Agent.git
cd AI-Research-Agent
```
2. Install dependencies
This project uses Poetry
```bash
pip install poetry
poetry install
```
3. Set up environment variables
Create a .env file in the root directory:
```bash
OPEN_API_KEY=your_openai_api_key
FIRECRAWL_API_KEY=your_firecrawl_api_key
```
4. Run the agent
```bash
poetry runn python main.py
```
or with Python:
```bash
python main.py
```

---

## 🔎 How It Works
1. Input a Research Topic
   - The user specifies a research query or topic (e.g "_Impacts of quantum computing on cryptography_"
2. Web Crawling (FireCrawl)
   - FireCrawl searches and extracts relevant documents, articles, and research papers
3. Data Structuring (Pydantic)
   - Extracted data is validated and structured into defined schemas for consistency
4. Reasoning Workflow (LangChain + LangGraph)
   - A workflow graph defines how the agent processes information step by step (search -> filter -> summarize -> refine)
   - LangChain handles LLM calls for summzarization and insight extraction
5. Final Output
   - A clean, summarized report of findings is returned, ready for further use
