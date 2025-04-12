import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título do app
st.title("Dashboard de IDESP - Escolas Públicas de SP (2023)")

# Carregamento dos dados
@st.cache_data
def carregar_dados():
    df = pd.read_csv("IDESP_ESCOLA_2023_0.csv", sep=";", encoding="latin1")
    df["ANOS_FINAIS"] = df["ANOS_FINAIS"].str.replace(",", ".").astype(float)
    return df

df = carregar_dados()

# Filtros
diretorias = df["NOME_DIRETORIA"].sort_values().unique()
diretoria_selecionada = st.selectbox("Selecione a Diretoria de Ensino", diretorias)

df_diretoria = df[df["NOME_DIRETORIA"] == diretoria_selecionada]

escolas = df_diretoria["NOME_ESCOLA"].sort_values().unique()
escolas_selecionadas = st.multiselect("Selecione uma ou mais escolas para comparar", escolas)

# Mostrar gráfico se escolas forem selecionadas
if escolas_selecionadas:
    df_selecionadas = df_diretoria[df_diretoria["NOME_ESCOLA"].isin(escolas_selecionadas)]

    # Média da diretoria
    media_diretoria = df_diretoria["ANOS_FINAIS"].mean()

    # Gráfico
    st.subheader("Comparação do IDESP (Anos Finais) - 2023")

    fig, ax = plt.subplots(figsize=(10, 5))
    escolas_plot = list(df_selecionadas["NOME_ESCOLA"])
    valores_plot = list(df_selecionadas["ANOS_FINAIS"])
    
    ax.bar(escolas_plot, valores_plot, color="orange", label="Escolas Selecionadas")
    ax.axhline(y=media_diretoria, color="blue", linestyle="--", label=f"Média da Diretoria ({media_diretoria:.2f})")
    ax.set_ylabel("IDESP")
    ax.set_xticklabels(escolas_plot, rotation=45, ha="right")
    ax.legend()
    st.pyplot(fig)

else:
    st.info("Selecione ao menos uma escola para comparar.")