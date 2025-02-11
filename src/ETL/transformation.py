# poetry run python transformation.py

import pandas as pd

def limpar_dados(dados):
    """
    Função para limpar os dados do DataFrame:
    1. Excluir as colunas 'Points' e 'Your' se existirem.
    2. Substituir valores contendo '@' ou '.com' por strings vazias ('') 
       sem excluir as linhas.
    
    Parâmetros:
    dados (pd.DataFrame): O DataFrame com os dados a serem limpos.

    Retorna:
    pd.DataFrame: O DataFrame limpo.
    """
    # Excluir as colunas 'Points' e 'Your' se existirem
    dados = dados.drop(columns=['Points', 'Your'], errors='ignore')

    # Função para remover valores específicos em cada célula
    def remover_emails(valor):
        if isinstance(valor, str) and ('@' in valor or '.com' in valor):
            return ''  # Substitui o valor por uma string vazia
        return valor

    # Aplicar a função a todas as células do DataFrame
    dados_limpos = dados.applymap(remover_emails)
    
    print("Dados limpos com sucesso! Nenhuma linha foi excluída.")
    return dados_limpos

# Exemplo de uso:
caminho = "C:/Users/Administrador/Downloads/Projetos Silverio/recruiting-academic-researchers-for-interviews.csv"
dados_csv = pd.read_csv(caminho, sep=';')  # Usa ',' como separador

# Limpar os dados
dados_limpos = limpar_dados(dados_csv)

# Exibir os dados limpos
print(dados_limpos.head())
