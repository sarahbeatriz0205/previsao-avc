import streamlit as st
import joblib
import pandas as pd

@st.cache_resource
def carregar_modelo():
    return joblib.load('models/modelo_avc.pkl')

modelo = carregar_modelo()

st.title("Previsão de Risco de AVC")
st.write("Insira as informações clínicas abaixo para avaliar o risco.")

with st.form("formulario_previsao"):
    age = st.number_input("Idade", min_value=0, max_value=120, value=16)
    hipertensao_op = st.selectbox("Possui Hipertensão?", ["Não", "Sim"])
    hypertension = 1 if hipertensao_op == "Sim" else 0

    cardiaco_op = st.selectbox("Possui Doença Cardíaca?", ["Não", "Sim"])
    heart_disease = 1 if cardiaco_op == "Sim" else 0

    avg_glucose_level = st.number_input(
        "Nível Médio de Glicose (mg/dL)",
        min_value=0.0,
        value=90.0,
        format="%.2f"
    )

    bmi = st.number_input(
        "IMC (Índice de Massa Corporal)",
        min_value=0.0,
        value=22.0,
        format="%.1f"
    )

    smoking_status = st.selectbox(
        "Status de Fumante",
        ["formerly smoked", "never smoked", "smokes", "Unknown"]
    )

    submit_button = st.form_submit_button("Avaliar Risco")

if submit_button:
    dados_paciente = pd.DataFrame({
        "age": [age],
        "hypertension": [hypertension],
        "heart_disease": [heart_disease],
        "avg_glucose_level": [avg_glucose_level],
        "bmi": [bmi],
        "smoking_status": [smoking_status]
    })

    previsao = modelo.predict(dados_paciente)
    probabilidade = modelo.predict_proba(dados_paciente)

    chance_avc = probabilidade[0][1] * 100

    st.subheader("Resultado da Análise:")

    st.metric("Probabilidade de AVC", f"{chance_avc:.2f}%")