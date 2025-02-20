import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_ollama import OllamaLLM

# Load and prepare data
df = pd.read_csv("car_price_dataset.csv").fillna(value=0)

# Initialize Ollama model

llm = OllamaLLM(model="llama3.2", temperature=0)

# Create pandas DataFrame agent
agent = create_pandas_dataframe_agent(
    llm=llm,
    df=df,
    verbose=True,
    allow_dangerous_code=True,
)

# Example query
response = agent.invoke("I want an electric car, which models can I get?")
print("Question: " + response["input"])
print("Answer: " + response["output"])