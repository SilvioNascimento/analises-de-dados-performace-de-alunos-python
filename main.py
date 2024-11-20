import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df_students_performance = pd.read_csv("./datasets/Cleaned_Students_Performance.csv")

math_score_max = df_students_performance["math_score"].max()
math_score_min = df_students_performance["math_score"].min()
max_math_score = st.sidebar.slider("Math Score", math_score_min, math_score_max, math_score_max)

df_scores = df_students_performance[df_students_performance["math_score"] <= max_math_score]
df_scores

