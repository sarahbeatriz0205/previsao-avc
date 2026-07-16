import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
import joblib

PASTA_DO_SCRIPT = Path(__file__).parent
RAIZ_REPOSITORIO = PASTA_DO_SCRIPT.parent
CAMINHO_CSV = RAIZ_REPOSITORIO / 'data' / 'raw' / 'healthcare-dataset-stroke-data.csv'

df = pd.read_csv(CAMINHO_CSV)

X = df[['age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi', 'smoking_status']]
y=df['stroke']

print(y.value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42,
    stratify=y
)

num_cols = ['age', 'hypertension','heart_disease', 'avg_glucose_level', 'bmi']
cat_cols = ['smoking_status']

num_pipe = Pipeline([
 ('imputer', SimpleImputer(strategy='median')),
 ('scaler', MinMaxScaler())
])
cat_pipe = Pipeline([
 ('imputer', SimpleImputer(strategy='most_frequent')),
 ('encoder', OneHotEncoder(handle_unknown='ignore'))
])
preprocessor = ColumnTransformer([
 ('num', num_pipe, num_cols),
 ('cat', cat_pipe, cat_cols)
])

model_lr = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(
        max_iter=1000, random_state=42, class_weight='balanced'
    ))
])

model_lr.fit(X_train, y_train)

y_pred = model_lr.predict(X_test)
y_proba = model_lr.predict_proba(X_test)[:, 1]