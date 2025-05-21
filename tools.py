from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
import json

# search tool
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information",
)

# searching from wiki
# top_k_result -> no of results
def wikipedia_lookup(query: str):
    wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
    result = wrapper.run(query)
    return json.dumps({
        "topic": query,
        "summary": result,
        "sources": ["Wikipedia"],
        "tools_used": ["wikipedia"]
    })

wiki_tool = Tool(
    name="wikipedia",
    func=wikipedia_lookup,
    description="Use this to look up encyclopedic information from Wikipedia"
)