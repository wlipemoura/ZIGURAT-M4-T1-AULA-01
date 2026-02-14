import io
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Configurações visuais
st.set_page_config(page_title="Análise Exploratória de Dados - Aula 1", layout="wide")

st.image("logo.png", width=320)

st.title("Análise Exploratória de Dados - Aula 1")


# Upload do arquivo
st.header("Upload do dataset")

uploaded_file = st.file_uploader(
    "Selecione um arquivo CSV",
    type=["csv"]
)

if uploaded_file is None:
    st.warning("Faça o upload de um arquivo CSV para continuar.")
    st.stop()


# Leitura do CSV
df = pd.read_csv(uploaded_file, sep=";")
st.success("Arquivo carregado com sucesso!")


# Visualização inicial
st.header("Visualização dos dados")

num_linhas = st.slider(
    "Quantidade de linhas para visualizar",
    min_value=5,
    max_value=50,
    value=10
)

st.dataframe(df.head(num_linhas))


# Informações do DataFrame
st.header("Estrutura do dataset")

with st.expander("Ver informações das colunas (df.info())"):
    buffer = io.StringIO()
    df.info(buf=buffer)
    st.text(buffer.getvalue())


# Contagem de valores
st.header("Análise de valores")

coluna = st.selectbox(
    "Escolha uma coluna para contagem de valores",
    df.columns
)

st.write(df[coluna].value_counts())


# Estatísticas descritivas
st.header("Estatísticas descritivas")

st.dataframe(df.describe())


# Visualizações gráficas
st.header("Visualizações")

tipo_grafico = st.selectbox(
    "Escolha o tipo de gráfico",
    [
        "Pairplot (hue categórico)",
        "Pairplot KDE (hue numérico)"
    ]
)

hue_col = st.selectbox(
    "Escolha a coluna para hue",
    df.columns
)

if st.button("Gerar gráfico"):
    sns.set_style("whitegrid")

    if tipo_grafico == "Pairplot (hue categórico)":
        sns.pairplot(df, hue=hue_col)
    else:
        sns.pairplot(df, hue=hue_col, kind="kde")

    st.pyplot(plt.gcf())
    plt.clf()
    
# Gráficos Matplotlib
st.header("Gráficos Matplotlib")

data = {
    'ZIGURAT ES': 10,
    'ZIGURAT BR': 15,
    'ZIGURAT USA': 5,
    'ZIGURAT FR': 20
}

names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(20, 5), sharey=True)

axs[0].bar(names, values)
axs[0].set_title("Barra")

axs[1].scatter(names, values)
axs[1].set_title("Dispersão")

axs[2].plot(names, values)
axs[2].set_title("Linha")

st.pyplot(fig)
plt.clf()
