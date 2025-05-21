from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
import os
from tools import search_tool,wiki_tool

# Load .env variables
load_dotenv()

# specify what you want from llm call
class ResearchResponse(BaseModel):
    topic:str
    summary:str
    sources:list[str]
    tools_used:list[str]

# to get started with the api call
llm = ChatOpenAI(
    model="llama3-70b-8192",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

# parse the class ResearchResponse so we can get our custom output
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            # system instructions on what AI should do
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use necessary tools. 
            Wrap the output in this format and provide no other text:\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())
# above line indiactes that it will take the instructions and parse acc to the format

# creation of agent
tools = [search_tool,wiki_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

# executer of agent {verbose -> thought process}
agent_executor = AgentExecutor(agent=agent,tools=tools,verbose=True)
# multiple prompt variables can be created {query}{name} but update above in the human part too
query = input("How can i Help? ")
raw_response = agent_executor.invoke({"query":query})
print(raw_response)

try:
    structured_response = parser.parse(raw_response["output"])
    print(structured_response)
except Exception as e:
    print("❌ Error parsing response:", e)
    print("🔍 Raw Response:", raw_response)