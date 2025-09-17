import pandas as pd
import streamlit as st

@st.cache_data
def load_csv(file) -> pd.DataFrame:
    """
    Load a CSV file (uploaded via Streamlit or a file path) into a DataFrame.
    Works for both uploaded file objects and string paths.
    """
    try:
        if hasattr(file, "read"):  # Streamlit uploader gives a file-like object
            return pd.read_csv(file)
        elif isinstance(file, str):  # If it's a file path
            return pd.read_csv(file)
        else:
            raise ValueError("Unsupported file type for CSV loading")
    except Exception as e:
        st.error(f"❌ Failed to load CSV: {e}")
        return pd.DataFrame()  # return empty dataframe on failure
