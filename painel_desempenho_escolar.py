import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Painel de Desempenho Escolar")

np.random.seed(11) 
alunos = [f"Aluno {i}" for i in range(1, 11)]
disciplinas = ["Matemática", "Português", "História", "Ciências"]

dados = {
    "Aluno": np.random.choice(alunos, size=40),
    "Nota": np.round(np.random.uniform(0, 10, size=40), 1),
    "Disciplina": np.random.choice(disciplinas, size=40)
}

df = pd.DataFrame(dados)


opcoes_disciplinas = ["Todas"] + disciplinas
disciplina_selecionada = st.selectbox("Selecione a disciplina", opcoes_disciplinas)


if disciplina_selecionada != "Todas":
    df_filtrado = df[df["Disciplina"] == disciplina_selecionada]
else:
    df_filtrado = df.copy()


st.subheader("Tabela de Notas")
st.dataframe(df_filtrado)


st.subheader("Gráfico de Notas por Aluno")
grafico = px.bar(df_filtrado, x="Aluno", y="Nota", color="Disciplina", barmode="group", title="Notas por Aluno")
st.plotly_chart(grafico)


st.subheader("Média Geral por Disciplina")
media_disciplinas = df.groupby("Disciplina")["Nota"].mean().round(2)
st.dataframe(media_disciplinas.reset_index().rename(columns={"Nota": "Média da Turma"}))
