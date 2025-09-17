import streamlit as st
import pandas as pd
from agent import query_agent
from utils import load_csv

st.set_page_config(page_title="Ask Me Anything", layout="wide")
st.title("Ask your data - AI-powered CSV assistant")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = load_csv(uploaded_file)
    
    if df.empty:
        st.warning("The uploaded CSV is empty or failed to load.")
    else:
        st.subheader("Preview of your data:")
        st.dataframe(df.head(20))  # show only first 20 rows to save space

        question = st.text_input("Ask a question about your data:")

        if question:
            with st.spinner("Processing your question..."):
                response = query_agent(df, question)  # ✅ correct parameter order
                st.subheader("Answer:")
                st.write(response)
