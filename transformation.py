
import pandas as pd

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


#  poetry run python transformation.py
