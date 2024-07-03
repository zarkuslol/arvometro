import sys
sys.path.append('.')

import datetime as dt

import streamlit as st
st.set_page_config(layout='wide')

from utils.db import DataBase
db = DataBase()

st.title('Ofertar muda')

col1, col2, col3 = st.columns(3)

with col1:
    donatarios = db.select('donatario')
    nomes = [donatarios[i][1] for i in range(len(donatarios))]
    nome_completo = st.selectbox(label='Nome Completo', options=nomes)
    foi_evento = st.selectbox(label='Foi em algum evento?', options=['Sim', 'Não'])

with col2:
    mudas = db.select('muda')
    muda = [mudas[i][1] for i in range(len(mudas))]
    nome_muda = st.selectbox(label='Tipo de muda', options=muda)
    nome_evento = st.text_input(label='Se sim, qual foi?')

with col3:
    qtd_doadas = st.number_input(label='Quantas mudas foram doadas?', min_value=1)

if st.button("Enviar"):
    data_doacao = dt.datetime.now()
    donatario = [donatarios[i] for i in range(len(donatarios)) if donatarios[i][1] == nome_completo]
    muda = [mudas[i] for i in range(len(mudas)) if mudas[i][1] == nome_muda]

    dados: tuple = (data_doacao, foi_evento, nome_evento, muda[0][0], donatario[0][0], qtd_doadas)

    try:
        db.update('muda', 'qtd_disponivel', (muda[0][-1] - qtd_doadas), muda[0][0])
        db.insert('doacao', dados)
        st.success("Dados enviados com sucesso!")
    except Exception as e:
        st.error(f"Erro ao enviar os dados: {e}")
