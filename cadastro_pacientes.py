import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Cadastro de Pacientes")


if 'pacientes' not in st.session_state:
    st.session_state['pacientes'] = []


with st.form("form_cadastro"):
    nome = st.text_input("Nome do paciente")
    idade = st.number_input("Idade", min_value=0, step=1)
    sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
    especialidade = st.selectbox("Especialidade médica", ["Clínica Geral", "Cardiologia", "Pediatria", "Dermatologia"])
    data_consulta = st.date_input("Data da consulta")
    convenio_check = st.checkbox("Convênio?")
    convenio_nome = ""
    if convenio_check:
        convenio_nome = st.text_input("Nome do convênio")

    submitted = st.form_submit_button("Cadastrar")

    if submitted:
        novo_paciente = {
            "Nome": nome,
            "Idade": idade,
            "Sexo": sexo,
            "Especialidade": especialidade,
            "Data da Consulta": data_consulta,
            "Convênio": convenio_nome if convenio_check else "Não"
        }
        st.session_state['pacientes'].append(novo_paciente)
        st.success("Paciente cadastrado com sucesso!")


if st.session_state['pacientes']:
    st.subheader("Pacientes Cadastrados")
    df_pacientes = pd.DataFrame(st.session_state['pacientes'])
    st.dataframe(df_pacientes)

    
    if st.button("Limpar Dados"):
        st.session_state['pacientes'] = []
        st.success("Dados apagados com sucesso!")
