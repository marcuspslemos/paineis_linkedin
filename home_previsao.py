import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------
# Simulação de dados
# ----------------------------
meses_2024 = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
vendas_2024 = [50, 55, 60, 58, 65, 70]

# Previsão para 2025 (simples extrapolação)
meses_2025 = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
vendas_previstas = [60, 63, 67, 72, 76, 80]

# ----------------------------
# Layout do Dashboard
# ----------------------------
st.title("📊 Dashboard de Vendas Preditivo")
st.write("Exemplo conceitual de como unir dados reais e previsões em um painel único.")

# KPIs
col1, col2 = st.columns(2)
col1.metric("Total de Vendas 2024", f"{sum(vendas_2024)} unidades")
col2.metric("Crescimento Previsto 2025", "+15%")

# ----------------------------
# Gráfico
# ----------------------------
fig, ax = plt.subplots(figsize=(6,3)

# Linha de vendas reais
ax.plot(meses_2024, vendas_2024, marker="o", color="blue", label="Vendas 2024")

# Linha de previsão
ax.plot(meses_2025, vendas_previstas, marker="o", linestyle="--", color="green", label="Previsão 2025")

ax.set_title("Evolução e Previsão de Vendas")
ax.set_ylabel("Unidades vendidas")
ax.legend()

st.pyplot(fig)

# ----------------------------
# Seleção de período (conceitual)
# ----------------------------
periodo = st.selectbox("Selecione o período:", ["1º semestre", "Ano inteiro"])
st.write(f"📌 Exibindo dados para: **{periodo}**")

# ----------------------------
# Botão de exportação
# ----------------------------
df = pd.DataFrame({
    "Meses_2024": meses_2024,
    "Vendas_2024": vendas_2024,
    "Meses_2025": meses_2025,
    "Previsão_2025": vendas_previstas
})

st.download_button(
    "📥 Baixar Relatório (CSV)",
    df.to_csv(index=False).encode("utf-8"),
    "relatorio_vendas.csv",
    "text/csv"
)
