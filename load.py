#  poetry run python load.py

import os
import pandas as pd
from transformation import limpar_dados  # Importando a função de transformação

def salvar_csv_na_pasta_data(dados, nome_arquivo):
    """
    Função para salvar um DataFrame em um arquivo CSV na pasta 'data' dentro do diretório atual.

    Parâmetros:
    dados (pd.DataFrame): O DataFrame a ser salvo.
    nome_arquivo (str): O nome do arquivo CSV (ex: 'dados_limpos.csv').

    Retorna:
    None
    """
    # Caminho para a pasta 'data' dentro do diretório atual
    caminho_pasta_data = os.path.join(os.getcwd(), 'data')
    
    # Verifica se a pasta 'data' existe, se não, cria
    if not os.path.exists(caminho_pasta_data):
        os.makedirs(caminho_pasta_data)
    
    # Caminho completo para salvar o arquivo CSV
    caminho_completo = os.path.join(caminho_pasta_data, nome_arquivo)
    
    try:
        # Salva o DataFrame como um arquivo CSV na pasta 'data'
        dados.to_csv(caminho_completo, index=False, sep=';')  # Usa ',' como separador
        print(f"Arquivo salvo com sucesso em: {caminho_completo}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def carregar_e_processar_csv(caminho_entrada, nome_arquivo_saida):
    """
    Carrega o arquivo CSV, aplica a transformação e salva o CSV resultante.

    Parâmetros:
    caminho_entrada (str): O caminho do arquivo CSV de entrada.
    nome_arquivo_saida (str): O nome do arquivo de saída.

    Retorna:
    None
    """
    try:
        # Carregar os dados do CSV de entrada
        dados = pd.read_csv(caminho_entrada, sep=';', skipinitialspace=True)
        print("Dados carregados com sucesso!")
        
        # Transformar os dados
        dados_limpos = limpar_dados(dados)
        
        # Salvar os dados limpos no arquivo CSV
        salvar_csv_na_pasta_data(dados_limpos, nome_arquivo_saida)
        
        print("Dados processados e salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")


