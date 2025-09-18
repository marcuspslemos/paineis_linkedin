import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ---- Título ----
st.title("📊 Dashboard de Predição de Vendas")

# ---- Dados simulados ----
meses = np.arange(1, 13)
vendas = np.array([100, 120, 140, 160, 200, 220, 250, 280, 300, 330, 370, 400])

df = pd.DataFrame({"Mês": meses, "Vendas": vendas})

# ---- Modelo preditivo (Regressão Linear) ----
X = df[["Mês"]]
y = df["Vendas"]

modelo = LinearRegression()
modelo.fit(X, y)

# Previsão para próximos 3 meses
meses_futuros = np.arange(13, 16).reshape(-1, 1)
previsao = modelo.predict(meses_futuros)

df_pred = pd.DataFrame({
    "Mês": meses_futuros.flatten(),
    "Vendas Previstas": previsao
})

# ---- Gráfico ----
fig, ax = plt.subplots()
ax.plot(df["Mês"], df["Vendas"], marker="o", label="Histórico de Vendas")
ax.plot(df_pred["Mês"], df_pred["Vendas Previstas"], marker="x", linestyle="--", color="green", label="Previsão")
ax.set_xlabel("Mês")
ax.set_ylabel("Vendas")
ax.legend()
st.pyplot(fig)

# ---- KPIs ----
col1, col2 = st.columns(2)
col1.metric("Crescimento Previsto", f"+{round(((previsao[-1] - vendas[-1]) / vendas[-1]) * 100, 2)}%")
col2.metric("Vendas em 15º mês", f"{int(previsao[-1])}")

# ---- Seleção de período ----
periodo = st.slider("Selecione o período de meses:", 1, 15, (1, 12))
st.write("Período selecionado:", periodo)
