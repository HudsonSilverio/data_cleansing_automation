import streamlit as st
import pandas as pd
import os
from load import salvar_csv_na_pasta_data
from transformation import limpar_dados

# Título da aplicação
st.title("Limpador de Dados - Remoção de E-mails")

# Upload do arquivo CSV
arquivo = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

if arquivo is not None:
    # Ler o arquivo carregado
    dados = pd.read_csv(arquivo)
    st.write("Prévia dos dados carregados:")
    st.write(dados.head())  # Mostra as primeiras linhas do CSV

    # Botão para processar o arquivo
    if st.button("Remover E-mails e Salvar CSV"):
        dados_limpos, colunas_originais = limpar_dados(dados)

        # Salvar o arquivo limpo
        nome_arquivo_saida = "dados_limpos.csv"
        salvar_csv_na_pasta_data(dados_limpos, nome_arquivo_saida)

        st.success(f"Arquivo processado e salvo como `{nome_arquivo_saida}` na pasta `data`.")
        st.write("Prévia dos dados limpos:")
        st.write(dados_limpos.head())  # Mostra a prévia dos dados processados

        # Link para download do arquivo processado
        caminho_completo = os.path.join(os.getcwd(), 'data', nome_arquivo_saida)
        with open(caminho_completo, "rb") as f:
            st.download_button("Baixar Arquivo Limpo", f, file_name=nome_arquivo_saida)


# poetry run python app.py