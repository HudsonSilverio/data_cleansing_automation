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

# Exemplo de execução do pipeline
if __name__ == "__main__":
    caminho_entrada = "C:/Users/Administrador/Downloads/Projetos Silverio/recruiting-academic-researchers-for-interviews.csv"
    nome_arquivo_saida = "dados_limpos.csv"
    executar_pipeline(caminho_entrada, nome_arquivo_saida)