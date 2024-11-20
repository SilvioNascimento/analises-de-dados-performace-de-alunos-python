import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

students_performance = pd.read_csv("./datasets/Cleaned_Students_Performance.csv")
students_performance
