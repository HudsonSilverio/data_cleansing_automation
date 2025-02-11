# poetry run python transformation.py

# import pandas as pd

# def limpar_dados(dados):
#     """
#     Função para limpar os dados do DataFrame:
#     1. Excluir as colunas 'Points' e 'Your' se existirem.
#     2. Substituir valores contendo '@' ou '.com' por strings vazias ('') 
#        sem excluir as linhas.
    
#     Parâmetros:
#     dados (pd.DataFrame): O DataFrame com os dados a serem limpos.

#     Retorna:
#     pd.DataFrame: O DataFrame limpo.
#     """
#     # Excluir as colunas 'Points' e 'Your' se existirem
#     dados = dados.drop(columns=['Points', 'Your'], errors='ignore')

#     # Função para remover valores específicos em cada célula
#     def remover_emails(valor):
#         if isinstance(valor, str) and ('@' in valor or '.com' in valor):
#             return ''  # Substitui o valor por uma string vazia
#         return valor

#     # Aplicar a função a todas as células do DataFrame
#     dados_limpos = dados.applymap(remover_emails)
    
#     print("Dados limpos com sucesso! Nenhuma linha foi excluída.")
#     return dados_limpos

# # Exemplo de uso:
# caminho = "C:/Users/Administrador/Downloads/Projetos Silverio/recruiting-academic-researchers-for-interviews.csv"
# dados_csv = pd.read_csv(caminho, sep=';', skipinitialspace=True)  # Usa ',' como separador

# # Limpar os dados
# dados_limpos = limpar_dados(dados_csv)

# # Exibir os dados limpos
# print(dados_limpos.head())

import pandas as pd

def limpar_dados(dados):
    """
    Função para limpar os dados do DataFrame:
    1. Excluir as colunas 'Points' e 'Your' se existirem.
    2. Substituir valores contendo '@' ou '.com' por strings vazias ('') 
       sem excluir as linhas.
    3. Unir as colunas '(UTC)3' com 'Minutes' e 'Spent' com 'Position'.
    
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
    
    # Unir as colunas '(UTC)3' e 'Minutes'
    if '(UTC)3' in dados_limpos.columns and 'Minutes' in dados_limpos.columns:
        dados_limpos['(UTC)3_Minutes'] = dados_limpos['(UTC)3'].astype(str) + ' ' + dados_limpos['Minutes'].astype(str)
    
    # Unir as colunas 'Spent' e 'Position'
    if 'Spent' in dados_limpos.columns and 'Position' in dados_limpos.columns:
        dados_limpos['Spent_Position'] = dados_limpos['Spent'].astype(str) + ' ' + dados_limpos['Position'].astype(str)
    
    # Remover as colunas originais após a união
    dados_limpos = dados_limpos.drop(columns=['(UTC)3', 'Minutes', 'Spent', 'Position'], errors='ignore')
    
    print("Dados limpos com sucesso! Nenhuma linha foi excluída.")
    return dados_limpos

# Exemplo de uso:
caminho = "C:/Users/Administrador/Downloads/Projetos Silverio/recruiting-academic-researchers-for-interviews.csv"
dados_csv = pd.read_csv(caminho, sep=';', skipinitialspace=True)  # Usa ';' como separador

# Limpar os dados
dados_limpos = limpar_dados(dados_csv)

# Exibir os dados limpos
print(dados_limpos.head())

