
import streamlit as st
import pandas as pd
import csv 
import os
#from load import salvar_csv_na_pasta_data  # Importe a função de salvar
#from transformation import limpar_dados  # Importe a função de limpeza

def salvar_csv_na_pasta_data(dados, nome_arquivo):
    """
    Salva um DataFrame em CSV na pasta 'data' dentro do diretório atual.
    """
    # Caminho para a pasta 'data' dentro do diretório atual
    caminho_pasta_data = os.path.join(os.getcwd(), 'data')
    
    # Verifica se a pasta 'data' existe, se não, cria
    if not os.path.exists(caminho_pasta_data):
        os.makedirs(caminho_pasta_data)
    
    # Caminho completo para salvar o arquivo CSV
    caminho_completo = os.path.join(caminho_pasta_data, nome_arquivo)
    
    try:
        # Salva o DataFrame como um arquivo CSV usando vírgula como separador
        # e forçando aspas para evitar quebrar colunas
        dados.to_csv(
            caminho_completo,
            index=False,
            sep=',',
            quoting=csv.QUOTE_ALL  # força o uso de aspas em todos os campos
        )
        print(f"Arquivo salvo com sucesso em: {caminho_completo}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

# Função para carregar e processar grandes arquivos CSV em pedaços (chunks)

def limpar_dados(dados):
    # Salvar a ordem original das colunas
    colunas_originais = dados.columns.tolist()

    # Função para remover emails
    def remover_emails(valor):
        if isinstance(valor, str) and ('@' in valor or '.com' in valor):
            return ''  # Substitui o valor por string vazia
        return valor

    # Aplicar a função a todas as células do DataFrame
    dados_limpos = dados.applymap(remover_emails)

    # Retornar tanto os dados limpos quanto a ordem original
    return dados_limpos, colunas_originais

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

