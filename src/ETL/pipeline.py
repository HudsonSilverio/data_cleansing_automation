# poetry run python pipeline.py 

import pandas as pd
import os
from transformation import limpar_dados
from load import salvar_csv_na_pasta_data

def executar_pipeline(caminho_entrada, nome_arquivo_saida):
    """
    Executa o pipeline ETL:
    1. Carrega os dados do arquivo CSV.
    2. Aplica a transformação para limpar os dados.
    3. Salva os dados transformados em um novo arquivo CSV.
    """
    try:
        # Carregar os dados
        dados = pd.read_csv(caminho_entrada, sep=';', skipinitialspace=True)
        print("Dados carregados com sucesso!")
        
        # Transformar os dados
        dados_limpos = limpar_dados(dados)
        
        # Salvar os dados limpos
        salvar_csv_na_pasta_data(dados_limpos, nome_arquivo_saida)
        
        print("Pipeline executado com sucesso!")
    except Exception as e:
        print(f"Erro na execução do pipeline: {e}")

# Função para solicitar o caminho do arquivo CSV
def obter_entrada():
    caminho_entrada = input("Digite o caminho do arquivo CSV a ser processado: ")
    nome_arquivo_saida = "dados_limpos.csv"
    return caminho_entrada, nome_arquivo_saida

if __name__ == "__main__":
    caminho_entrada, nome_arquivo_saida = obter_entrada()
    executar_pipeline(caminho_entrada, nome_arquivo_saida)
