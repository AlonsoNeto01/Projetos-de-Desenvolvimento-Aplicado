import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Painel de Análise")


arquivo = st.file_uploader("Faça upload do arquivo Bike_rent.csv", type=['csv'])

if arquivo is not None:
    df = pd.read_csv(arquivo)

    st.subheader("Prévia dos dados")
    st.dataframe(df.head())

    st.subheader("Estatísticas descritivas")
    st.write(df.describe())

    # Filtros interativos
    st.sidebar.title("Filtros")
    estacoes = {1: 'Primavera', 2: 'Verão', 3: 'Outono', 4: 'Inverno'}
    df['Estacao'] = df['season'].map(estacoes)

    estacao_opcao = st.sidebar.multiselect("Filtrar por estação", df['Estacao'].unique(), default=df['Estacao'].unique())
    feriado = st.sidebar.selectbox("É feriado?", options=["Todos", "Sim", "Não"])

    df_filtrado = df[df['Estacao'].isin(estacao_opcao)]
    if feriado == "Sim":
        df_filtrado = df_filtrado[df_filtrado['holiday'] == 1]
    elif feriado == "Não":
        df_filtrado = df_filtrado[df_filtrado['holiday'] == 0]

    st.subheader("Gráfico: Total de Aluguéis por Mês")
    df_filtrado['Mês'] = df_filtrado['mnth']
    fig_meses = px.bar(df_filtrado, x="Mês", y="cnt", color="Estacao", title="Quantidade de Aluguéis por Mês")
    st.plotly_chart(fig_meses)

    st.subheader("Gráfico Personalizado")
    col_x = st.selectbox("Escolha o eixo X", df_filtrado.columns)
    col_y = st.selectbox("Escolha o eixo Y", df_filtrado.select_dtypes(include=np.number).columns)

    if st.button("Gerar Gráfico"):
        fig_custom = px.scatter(df_filtrado, x=col_x, y=col_y, color="Estacao", title=f"{col_y} vs {col_x}")
        st.plotly_chart(fig_custom)

       
        if df_filtrado[col_x].dtype in [np.float64, np.int64]:
            correlacao = df_filtrado[col_x].corr(df_filtrado[col_y])
            st.markdown(f"**Correlação entre {col_x} e {col_y}:** {correlacao:.2f}")
            if correlacao > 0.5:
                st.success("Correlação positiva forte.")
            elif correlacao < -0.5:
                st.warning("Correlação negativa forte.")
            else:
                st.info("Correlação fraca ou inexistente.")
        else:
            st.info("Correlação só pode ser calculada entre colunas numéricas.")
