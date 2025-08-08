import os
from dotenv import load_dotenv
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = OpenAI(
    openai_api_key=OPENAI_API_KEY, temperature=0.7
)  

tools = load_tools(["wikipedia", "llm-math"], llm=llm)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

prompt = input("The Wikipedia research task: ")

agent.run(prompt)