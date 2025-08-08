import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = OpenAI(
    openai_api_key=OPENAI_API_KEY, temperature=0.7
)   

prompt = PromptTemplate(
    input_variables=["content", "customer_name", "agent_name"],
    template="""
        You are an AI assistant that's optimized to write concise, friendly & professional emails to customers.

        Write an email to a customer with the name {customer_name} that contains the following, optimized content: {content} 

        The email signature should contain the name of the customer agent who wrote the email: {agent_name}
    """
)

content = input("Enter the content of the email: ")
customer_name = input("Enter the customer's name: ")
agent_name = input("Enter the agent's name: ")

response = llm(prompt.format(content=content, customer_name=customer_name, agent_name=agent_name))

print("Generated Email:")
print(response)