# Research Agent Project

This project builds a **LangChain Agent** that can:
- Take in a research question
- Search the web (DuckDuckGo)
- Pull information from Wikipedia
- Save results to a file
- Return structured responses in JSON

---

## Setup

1. Clone the repo
   ```bash
   git clone https://github.com/wafadalilahabet-jpg/agents_project
   cd agents_project
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Add your API keys (e.g., OpenAI, Anthropic) inside `.env`.

---

## Run

```bash
python main.py
```

You’ll be prompted for a research query.  
The agent will:

- Use tools (`search`, `wiki`, `save_text_to_file`)  
- Save outputs to `research_output.txt`  
- Return a structured response like:

```json
{
  "topic": "AI in healthcare",
  "summary": "AI is being applied in diagnostics, drug discovery, and patient monitoring.",
  "sources": ["DuckDuckGo", "Wikipedia"],
  "tools_used": ["search", "wiki", "save_text_to_file"]
}
```

---

## Project Structure

- **main.py** → runs the research agent pipeline  
- **tools.py** → defines search, wiki, and save tools  
- **research_output.txt** → stores saved results  
- **.env.example** → template for environment variables  
- **requirements.txt** → dependencies  

---

## Future Ideas

- Add more tools (arXiv, PubMed, news APIs)  
- Summarize sources automatically  
- Build a front-end (Streamlit or Gradio)


