import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Projeto de Desenvolvimento Aplicado, BSI 2022')
st.write('disciplina voltada para a aplicação de ferramentas de ciências de dados')

st.header('Este é um header')

st.subheader('Este é um subheader')
st.text("Apenas um texto sem formatação")
st.markdown('Este é um texto *formatado** com markdown')


# DATASET

dados = {
    'Nome' : ['Fulano', 'James', 'Nicoli'],
    'Idade' : [35, 52, 20],
    'Salário' : [4000, 11000, 1800],
    'Cidade' : ['Oriximina', 'Santarem', 'Obidos']
}


# DATAFRAME
df = pd.DataFrame(dados)
st.dataframe(df) #tabela dinâmica
st.table(df) #tabela estática

# Gráfico Barra

fig, ax = plt.subplots()
ax.bar(df['Nome'], df['Salário'])
st.pyplot(fig)

# INTERATIVIDADE com botão
if st.button(
    'CLique aqui para ver o gráfico de barras'):

    st.write('GRÁFICO ABERTO')

# INTERATIVIDADE com barra deslizante
idade = st.slider('Selecione o valor da idade', 0, 100, 23)
st.write(f'Idade selecionada: {idade}')

# INTERATIVADE com barra deslizante
opcoes = ['Oriximina', 'Santarem', 'Obidos']
Cidade = st.selectbox('Selecione a cidade', opcoes)

# FILTRO
st.sidebar.header('Filtros')
pessoas = ['Fulano', 'Beltrano', 'Ciclano']
pessoa_selecionada = st.sidebar.selectbox('Selecione a pessoa', pessoas)


##Lendo dados externos
df = pd.read_csv("Pasta1.csv", sep=";")

idade_min = st.slider("Idade minima", 0, 100, 30)
df_filtrado = df[df["idade"]> idade_min]
st.dataframe(df_filtrado)