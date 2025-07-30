import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Loads .env file

def query_agent(df: pd.DataFrame, question: str) -> str:
    llm = OpenAI(temperature=0, api_key=os.getenv("OPENAI_API_KEY"))
    agent = create_pandas_dataframe_agent(llm, df, verbose=False)
    try:
        return agent.run(question)
    except Exception as e:
        return f"❌ Error: {str(e)}"
