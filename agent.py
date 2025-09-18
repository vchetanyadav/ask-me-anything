import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Loads environment variables from .env

def query_agent(df: pd.DataFrame, question: str) -> str:
    """
    Query the DataFrame using LangChain Pandas DataFrame Agent and OpenAI LLM.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return " Error: OPENAI_API_KEY not set in environment."

    try:
        llm = ChatOpenAI(
            temperature=0,
            api_key=api_key,
            model="gpt-3.5-turbo"
        )
        agent = create_pandas_dataframe_agent(
            llm,
            df,
            verbose=False,
            allow_dangerous_code=True   
        )
        return agent.run(question)
    except Exception as e:
        return f"❌ Error: {str(e)}"


