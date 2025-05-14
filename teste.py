import streamlit as st
import pandas as pd
import plotly.express as px

# Título do aplicativo
st.title("📊 Analisador")

arquivo = st.file_uploader("Faça upload do arquivo (CSV)", type=["csv"])


if arquivo is not None:
    
    df = pd.read_csv(arquivo)

    # Exibir a tabela com os primeiros registros
    st.subheader("📋 Prévia dos Dados")
    st.dataframe(df.head())

    # Estatísticas Descritivas
    st.subheader("📊 Estatísticas Descritivas")
    st.write(df.describe())

    # Limpeza dos dados
    df = df.dropna()

    # Seleção das colunas para o eixo X e Y do gráfico
    st.subheader("🎨 Gerar Gráfico")
    eixo_x = st.selectbox("Escolha a coluna para o eixo X", df.columns)
    eixo_y = st.selectbox("Escolha a coluna para o eixo Y", df.columns)

    cor = st.selectbox("Escolha a coluna para colorir (opcional)", [None] + list(df.columns))

    # Botão para gerar gráfico
    if st.button("Gerar Gráfico"):
        try:
            if cor:
                fig = px.bar(df, x=eixo_x, y=eixo_y, color=cor, title="Gráfico de Barras")
            else:
                fig = px.bar(df, x=eixo_x, y=eixo_y, title="Gráfico de Barras")
            st.plotly_chart(fig)
        except Exception as e:
            st.error(f"Erro ao gerar gráfico: {e}")
else:
    st.warning("Por favor, envie um arquivo CSV para iniciar a análise.")