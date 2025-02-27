
import streamlit as st
import pandas as pd
import os
from load import salvar_csv_na_pasta_data  # Importe a função de salvar
from transformation import limpar_dados  # Importe a função de limpeza

# Função para carregar e processar grandes arquivos CSV em pedaços (chunks)
def processar_csv_em_chunks(arquivo, chunksize=50000):
    # Ler arquivo em pedaços menores
    for chunk in pd.read_csv(arquivo, chunksize=chunksize):
        # Processar cada pedaço (aqui, você pode aplicar as funções de limpeza)
        chunk_limpo, colunas_originais = limpar_dados(chunk)
        yield chunk_limpo  # Retorna o pedaço limpo para ser processado

# Estilo visual (Fundo escuro, botões coloridos, etc)
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #2e2e2e;
    }
    .sidebar .sidebar-content {
        background-color: #333333;
    }
    h1 {
        color: #ffffff;
    }
    .stButton>button {
        background-color: #FF5733;
        color: white;
    }
    .stTextInput>input {
        background-color: #333333;
        color: white;
        border: 1px solid #FF5733;
    }
    .stDownloadButton>button {
        background-color: #28a745;
        color: white;
    }
    .stText {
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True
)

# Título da aplicação
st.title("🚀 **Limpador de Dados** - Suporte a Arquivos Grandes")

# Input para o caminho do arquivo local
caminho_arquivo = st.text_input("📁 **Digite o caminho do arquivo CSV**", "")

if caminho_arquivo:
    # Verifica se o arquivo existe
    if os.path.exists(caminho_arquivo):
        st.write("🔄 **Carregando dados...** Isso pode levar um tempo, aguarde um momento.")

        try:
            # Inicializar a lista para armazenar os pedaços processados
            dados_processados = []

            # Processar o CSV em pedaços (chunks) e aplicar a limpeza
            for chunk in processar_csv_em_chunks(caminho_arquivo, chunksize=50000):
                dados_processados.append(chunk)  # Adiciona cada pedaço limpo na lista

                # Exibe apenas a prévia de um chunk para evitar travamentos
                st.write("🔍 **Prévia do arquivo processado:**")
                st.write(chunk.head(10))  # Mostra as primeiras linhas de cada pedaço limpo

            # Combina todos os pedaços processados em um único DataFrame
            df_final = pd.concat(dados_processados, ignore_index=True)

            # Salvar o arquivo limpo
            nome_arquivo_saida = "dados_limpos.csv"
            salvar_csv_na_pasta_data(df_final, nome_arquivo_saida)

            st.success(f"🎉 **Arquivo limpo e salvo** como `{nome_arquivo_saida}` na pasta `data`.")
            st.write("🔍 **Prévia dos dados limpos:**")
            st.write(df_final.head(10))  # Mostra a prévia dos dados limpos

            # Link para download do arquivo processado
            caminho_completo = os.path.join(os.getcwd(), 'data', nome_arquivo_saida)
            with open(caminho_completo, "rb") as f:
                st.download_button("⬇️ **Baixar Arquivo Limpo**", f, file_name=nome_arquivo_saida)

        except Exception as e:
            st.error(f"❌ **Erro ao processar o arquivo:** {e}")
    else:
        st.error("⚠️ **O arquivo informado não foi encontrado.** Verifique o caminho e tente novamente.")


# poetry run streamlit run app.py

