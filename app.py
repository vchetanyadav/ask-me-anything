import streamlit as st
import pandas as pd
from agent import quer_agent
from utils import load_csv

st.set_page_config(page_title="Ask Me Anything ", layout="wide")
st.title("Ask your data - AI-powered CSV assistant")
uploaded_file=st.file_uploader("Upload a csv file", type=["csv"])

if uploaded_file:
    df=load_csv(uploaded_file)
    st.dataframe(df)

    question = st.text_input("Ask a question about your data:")

    if question:
        with st.spinner("Processing your question..."):
            repponse = quer_agent(question, df)
            st.write(repponse)
            
