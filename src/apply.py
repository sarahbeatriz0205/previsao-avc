import joblib
import pandas as pd
modelo_carregado = joblib.load('models/modelo_avc.pkl')

paciente = pd.DataFrame([{
    'age': 16,
    'hypertension': 0,
    'heart_disease': 0,
    'avg_glucose_level': 83.75 ,
    'smoking_status': 'never smoked',
    'bmi': 24.0,
    'stroke': 0
}])

dados=modelo_carregado.predict_proba(
    paciente)

print(dados)

prob_avc = modelo_carregado.predict_proba(
    paciente)[0][1]
print(f"Risco de AVC: {prob_avc:.1%}")