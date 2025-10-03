"""
Tools for Research Agent
========================

Provides:
1. DuckDuckGo search tool.
2. Wikipedia query tool.
3. Save-to-file tool for structured outputs.
"""

# -------------------- Imports --------------------
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime


# -------------------- Save Tool --------------------
def save_to_txt(data: str, filename: str = "research_output.txt"):
    """Save research data into a text file with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file."
)


# -------------------- Search Tool --------------------
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information."
)


# -------------------- Wikipedia Tool --------------------
api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,               # Only return most relevant
    doc_content_chars_max=100      # Limit content size
)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
