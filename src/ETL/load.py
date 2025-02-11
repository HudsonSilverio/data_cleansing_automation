# poetry run python load.py

import os
import pandas as pd
from transformation import dados_limpos  # Corrigindo a importação do módulo correto

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

# Exemplo de uso:
# Supondo que `dados_limpos` seja o DataFrame com os dados limpos
nome_arquivo = 'dados_limpos.csv'

# Salvar o DataFrame limpo no CSV dentro da pasta 'data'
salvar_csv_na_pasta_data(dados_limpos, nome_arquivo)
