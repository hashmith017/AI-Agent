# AI Agent

This project implements a research assistant AI agent powered by LangChain and an LLM (Llama 3 via Groq API). 
The agent accepts user queries, leverages web search and Wikipedia tools to gather information, and outputs structured, JSON-formatted research summaries.
I have added search_tool,wiki_tool which helps to search the web easily and gets the answer

## Features

- Uses LangChain's tool-calling agents to integrate multiple tools
- Fetches information from Wikipedia and DuckDuckGo Search
- Enforces strict JSON output formatting via Pydantic for structured data
- Verbose mode enabled for debugging and understanding agent thought process
- Easy to extend with additional tools or different LLM models

## Requirements

- Python 3.9+
- API keys (Groq API for Llama 3 model)
- Required Python packages (listed in `requirements.txt`)

## Installation
1.Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate 

2.Install dependencies

pip install -r requirements.txt

3.Create a .env file in the root directory

GROQ_API_KEY=your_groq_api_key_here

## Usage
Run the main script:       python main1.py

You will be prompted:      How can I help?

Type your research query, e.g.:India population

The agent will fetch relevant information, process it, and print a structured research summary.

## SAMPLE OUTPUT
(venv) PS D:\2.COLLEGE\AI MODEL> python .\main1.py
How can i Help? India population

> Entering new AgentExecutor chain...

Invoking: `search` with `India population`

India's population exceeded that of the entire continent of Africa by 200 million people in 2010. [104] However, because Africa's population growth is extremely high compared to the rest of the world, [105] [106] it is expected to surpass both China and India by the early 2030s. [107] Find out the current population of India, its growth rate, net migration rate, and historical data. 
Compare India with other countries in the region and the world in terms of population size and density. Find the latest population estimates and projections of India based on UN data and census. Learn about the population growth rate, net change, share and density of India over time. Learn about India, the most populous country in the world, with over 1.4 billion people. 
Explore its diverse history, culture, geography, economy and challenges on Wikipedia. India Population 2025: Growth Trends from 1960 to 2025. Population of India in 2025 is estimated to reach 1.45 billion therefore making it the most populous country in the world, surpassing China, which is projected to have 1.41 billion people. 
India's rapid population growth in the second half of the 20th century was driven by improved healthcare, lower infant mortality rates, and increased ...{"topic": "India Population", "summary": "India's population is expected to surpass China's by 2025, with an estimated 1.45 billion people. The country's rapid population growth is driven by improved healthcare and lower infant mortality rates.", "sources": ["Wikipedia", "UN data and census"], "tools_used": ["search"]}

> Finished chain.
topic='India Population' summary="India's population is expected to surpass China's by 2025, with an estimated 1.45 billion people. The country's rapid population growth is driven by improved healthcare and lower infant mortality rates." sources=['Wikipedia', 'UN data and census'] tools_used=['search']

output 1
![image](https://github.com/user-attachments/assets/3e00b7e2-e038-43db-a6dd-ecf73723f2a2)

output 2
![image](https://github.com/user-attachments/assets/4448d340-d17b-4438-8add-e74249f858ec)

output 3
![image](https://github.com/user-attachments/assets/1b3b5f1f-39ef-4f15-b8af-7fc63f783f81)




