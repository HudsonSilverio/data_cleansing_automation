
import os
import pandas as pd
import csv
from transformation import limpar_dados

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

def carregar_e_processar_csv(caminho_entrada, nome_arquivo_saida):
    """
    Carrega o arquivo CSV, aplica a transformação e salva o CSV resultante.
    """
    try:
        # Carrega os dados do CSV de entrada usando vírgula como separador
        # Remova skipinitialspace=True se não for necessário
        dados = pd.read_csv(caminho_entrada, sep=',')
        print("Dados carregados com sucesso!")
        
        # Transformar os dados e obter a ordem original das colunas
        dados_limpos, colunas_originais = limpar_dados(dados)
        
        # Verifica quais colunas foram criadas
        novas_colunas = [c for c in dados_limpos.columns if c not in colunas_originais]
        # Gera uma lista final de colunas: as originais + as novas
        ordem_final = colunas_originais + novas_colunas
        
        # Reindexa para manter a ordem
        dados_limpos = dados_limpos.reindex(columns=ordem_final, fill_value='')
        
        # Salvar os dados limpos no arquivo CSV
        salvar_csv_na_pasta_data(dados_limpos, nome_arquivo_saida)
        
        print("Dados processados e salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")



