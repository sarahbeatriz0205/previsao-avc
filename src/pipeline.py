import pandas as pd
from pathlib import Path

PASTA_DO_SCRIPT = Path(__file__).parent
RAIZ_REPOSITORIO = PASTA_DO_SCRIPT.parent
CAMINHO_CSV = RAIZ_REPOSITORIO / 'data' / 'processed' / 'dados_tratados.csv'

df = pd.read_csv(CAMINHO_CSV)

df= pd.get_dummies(
    df,
    columns=['gender', 'ever_married','work_type', 'Residence_type', 'smoking_status', 'faixa_etaria', 'faixa_glicemica', 'faixa_bmi'],
    drop_first=True
)

# Removi as colunas numéricas que já possuiam uma faixa associada a elas
df.drop(columns=['age', 'bmi', 'avg_glucose_level'], inplace=True)

print(df)

# Maioria booleans agora
print(df.dtypes)
print(df.shape)