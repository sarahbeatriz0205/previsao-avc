# Quais as chances de você ter um AVC?

O projeto acadêmico versionado neste repositório para a disciplina de **Técnicas de Análise de Dados** do curso de **Análise e Desenvolvimento de Sistemas (IFRN)** têm como objetivo prever **quais as chances de alguém ter um AVC** baseado nas informações de **_idade, se possui hipertensão e/ou doenças cardíacas, se fuma, índice de massa corpórea e nível de glicose._**

## Arquitetura

```text
├── app/
│   └── index.py
│
├── data/
│   ├── processed/
│   ├── raw/
│
├── models/
│   └── modelo_avc.pkl
│
├── notebooks/
│   └── eda_insights.ipynb
│
├── src/
│   ├── apply.py
│   ├── pipeline.py
│   └── train.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Como executar
1. **Clone este repositório na sua máquina local:**
```bash
https://github.com/sarahbeatriz0205/previsao-avc.git
```

2. **Ao clonar, abra no VSCode e no terminal, crie um ambiente virtual Python:**
```bash
python -m venv .venv
```

3. **Ative o ambiente criado:**
- **Se estiver no Windows**
```bash
venv\Scripts\activate
```

- **Se estiver no Linux**
```bash
source venv/bin/activate
```

4. **Instale as dependências contidas no arquivo ```requirements.txt```**
```bash
pip install -r requirements.txt
```

5. **Entre dentro da pasta ```app```:**
```bash
cd app
```

6. **Execute o comando:**
```bash
streamlit run index.py
```

### E pronto! Você já pode utilizar a aplicação tranquilamente
