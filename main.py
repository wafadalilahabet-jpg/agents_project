"""
Research Agent
==============

This script:
1. Uses LangChain + OpenAI (or Anthropic) LLMs.
2. Runs a tool-using research assistant agent.
3. Supports search (DuckDuckGo), Wikipedia, and saving results.
4. Returns structured responses using Pydantic.
"""

# -------------------- Imports --------------------
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic  # Optional alternative
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool


# -------------------- Environment --------------------
# Load API keys from .env
load_dotenv()


# -------------------- Output Schema --------------------
class ResearchResponse(BaseModel):
    """Structured response format for research results."""
    topic: str            # The research topic
    summary: str          # A summary of findings
    sources: list[str]    # A list of sources consulted
    tools_used: list[str] # A list of tools that were used


# -------------------- Model --------------------
# Primary model (OpenAI GPT-4o-mini here, can swap later)
model = ChatOpenAI(model="gpt-4o-mini")
# model = ChatAnthropic()   # Example: Claude


# -------------------- Parser --------------------
parser = PydanticOutputParser(pydantic_object=ResearchResponse)


# -------------------- Prompt --------------------
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that generates structured research reports.
            Use the provided tools when needed.
            Return answers ONLY in this format:
            {format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),   # Prior conversation
        ("human", "{query}"),                # User query
        ("placeholder", "{agent_scratchpad}")# Agent tool calls / scratch work
    ]
).partial(format_instructions=parser.get_format_instructions())


# -------------------- Tools --------------------
tools = [search_tool, wiki_tool, save_tool]


# -------------------- Agent --------------------
agent = create_tool_calling_agent(
    llm=model,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


# -------------------- Run --------------------
def run_research():
    """Run the research agent interactively."""
    query = input("What research are you interested in? ")

    # Get raw agent response
    raw_response = agent_executor.invoke({"query": query})

    # Try to parse into structured format
    try:
        structured_response = parser.parse(raw_response["output"])
        print("\n--- Structured Response ---")
        print(structured_response.json(indent=2))
    except Exception as e:
        print("Error parsing:", e)
        print("Raw response:", raw_response)


if __name__ == "__main__":
    run_research()
