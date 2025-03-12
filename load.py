
import os
import pandas as pd
import csv


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





