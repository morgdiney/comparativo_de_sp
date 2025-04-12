import pandas as pd
import matplotlib.pyplot as plt

# Carrega a planilha (você já deve ter o DataFrame df carregado)
df = pd.read_csv("IDESP_ESCOLA_2023_0.csv", sep=";", encoding="latin1")

# Filtrar a diretoria de interesse
df_itapevi = df[df["NOME_DIRETORIA"] == "ITAPEVI"].copy()

# Converter coluna de IDESP para float (ajustando a vírgula para ponto)
df_itapevi["ANOS_FINAIS"] = df_itapevi["ANOS_FINAIS"].str.replace(",", ".").astype(float)

# Nome da escola que queremos destacar
escola_alvo = "HENRIQUE SAMMARTINO ALFERES"

# Obter valor da escola-alvo
idesp_escola = df_itapevi[df_itapevi["NOME_ESCOLA"].str.upper() == escola_alvo.upper()]["ANOS_FINAIS"].values[0]

# Calcular média da diretoria
media_idesp = df_itapevi["ANOS_FINAIS"].mean()

# Plotar gráfico
plt.figure(figsize=(8, 5))
plt.bar(["Média Itapevi", escola_alvo], [media_idesp, idesp_escola], color=["skyblue", "orange"])
plt.title("Comparação do IDESP (Anos Finais) - 2023")
plt.ylabel("IDESP")
plt.ylim(0, 5)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Adicionar rótulos de valor nas barras
for i, valor in enumerate([media_idesp, idesp_escola]):
    plt.text(i, valor + 0.1, f"{valor:.2f}", ha='center')

plt.show()


