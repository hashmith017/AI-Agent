from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

# Choose the required LLM
# llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
llm = ChatOpenAI(model="gpt-4o-mini")  # Use the model of choice

# Invoke the LLM with a prompt
response = llm.invoke("What is the meaning of life?")

# Print the response
print(response.content)