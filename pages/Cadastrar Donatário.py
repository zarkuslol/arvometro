import sys
sys.path.append('.')

import streamlit as st
st.set_page_config(layout='wide')

from utils.db import DataBase
db = DataBase()

def formatar_telefone(telefone):
    telefone = telefone.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
    if len(telefone) == 11:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    return telefone

st.title('Cadastrar novo donatário')

col1, col2 = st.columns(2)

with col1:
    nome_completo = st.text_input("Nome Completo")
    bairro = st.selectbox("Bairro", ["Pirapitinga", "Drummond", "Centro"])

with col2:
    data_nascimento = st.date_input("Data de Nascimento", format='DD/MM/YYYY', min_value=None)
    telefone = st.text_input("Telefone", placeholder="(34) 99999-9999")
    telefone = formatar_telefone(telefone)

if st.button("Enviar"):
    dados: tuple = (nome_completo, data_nascimento.strftime('%Y-%m-%d'), bairro, telefone)
    try:
        db.insert('donatario', dados)
        st.success("Dados enviados com sucesso!")
    except Exception as e:
        st.error(f"Erro ao enviar os dados: {e}")
