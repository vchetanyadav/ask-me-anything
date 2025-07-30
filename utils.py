import pandas as pd
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def query_agent(df: pd.DataFrame, question: str) -> str:
    llm=OpenAI(temperature=0)
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)
    try:
        return agent.run(question)
    except Exception as e:
        return f" Error: {str(e)}"
