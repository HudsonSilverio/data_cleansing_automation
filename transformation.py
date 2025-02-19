#  poetry run python transformation.py


def limpar_dados(dados):
    # Salvar a ordem original das colunas
    colunas_originais = dados.columns.tolist()

    # Excluir as colunas 'Points' e 'Your' se existirem
    dados = dados.drop(columns=['Points', 'Your'], errors='ignore')

    # Função para remover emails
    def remover_emails(valor):
        if isinstance(valor, str) and ('@' in valor or '.com' in valor):
            return ''  # Substitui o valor por string vazia
        return valor

    # Aplicar a função a todas as células do DataFrame
    dados_limpos = dados.applymap(remover_emails)

    # Unir colunas específicas
    if '(UTC)3' in dados_limpos.columns and 'Minutes' in dados_limpos.columns:
        dados_limpos['(UTC)3_Minutes'] = dados_limpos['(UTC)3'].astype(str) + ' ' + dados_limpos['Minutes'].astype(str)

    if 'Spent' in dados_limpos.columns and 'Position' in dados_limpos.columns:
        dados_limpos['Spent_Position'] = dados_limpos['Spent'].astype(str) + ' ' + dados_limpos['Position'].astype(str)

    # Remover as colunas originais após a união
    dados_limpos = dados_limpos.drop(columns=['(UTC)3', 'Minutes', 'Spent', 'Position'], errors='ignore')

    # **Reordenar o DataFrame para manter a estrutura original**
    dados_limpos = dados_limpos.reindex(columns=colunas_originais, fill_value='')

    return dados_limpos


#  poetry run python transformation.py
