# Usa a imagem oficial do Python 3.12.1 como base
FROM python:3.12.1-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala o Poetry
RUN pip install --no-cache-dir poetry

# Copia todos os arquivos do projeto para o contêiner
COPY . /app

# Instala as dependências sem criar um ambiente virtual e sem instalar o próprio projeto
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root

# Expõe a porta que será usada pelo Streamlit (se aplicável)
EXPOSE 8501

# Define o comando de inicialização do contêiner
CMD ["poetry", "run", "streamlit", "run", "app.py"]

