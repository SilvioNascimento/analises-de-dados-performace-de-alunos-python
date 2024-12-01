import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página da aplicação web
st.set_page_config(
    page_title="Performace dos estudantes",
    page_icon="📊",
    layout="wide"
)

# Carregando o arquivo .csv
df_students_performance = pd.read_csv("./datasets/Cleaned_Students_Performance.csv")

# Substituindo os valores 0 por 'feminine' e 1 por 'masculine' na coluna 'gender'
df_students_performance['gender'] = df_students_performance['gender'].replace({0: 'feminine', 1: 'masculine'})

# Configurando o valor máximo e o mínimo de math_score no slider
math_score_max = df_students_performance["math_score"].max()
math_score_min = df_students_performance["math_score"].min()
max_math_score = st.sidebar.slider("Math Score", math_score_min, math_score_max, math_score_max)

# Configurando o valor máximo e o mínimo de reading_score no slider
reading_score_max = df_students_performance["reading_score"].max()
reading_score_min = df_students_performance["reading_score"].min()
max_reading_score = st.sidebar.slider("Reading Score", reading_score_min, reading_score_max, reading_score_max)

# Configurando o valor máximo e o mínimo de writing_score no slider
writing_score_max = df_students_performance["writing_score"].max()
writing_score_min = df_students_performance["writing_score"].min()
max_writing_score = st.sidebar.slider("Writing Score", writing_score_min, writing_score_max, writing_score_max)

# Permitindo a filtração de dados dos sliders na tabela
df_scores = df_students_performance[(df_students_performance["math_score"] <= max_math_score) & (df_students_performance["reading_score"] <= max_reading_score) & (df_students_performance["writing_score"] <= max_writing_score)]
df_scores


# Criando gráficos básicos em relação com as pontuações de matemática

# Agrupando por 'math_score' e 'gender' para incluir a coluna 'gender'
df_grouped_math = df_scores.groupby(['math_score', 'gender']).size().reset_index(name='count')

# Criando o gráfico de barras
fig1 = px.bar(df_grouped_math, x="math_score", y="count", color="gender", title="Gráfico de barras de pontuação de matemática por contagem")
fig1