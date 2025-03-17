# Usando uma imagem oficial do Python 3.12 como base
FROM python:3.12

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Instalar dependências do Poetry
RUN pip install --no-cache-dir poetry

# Copiar arquivos do projeto para dentro do container
COPY pyproject.toml poetry.lock /app/

# Instalar as dependências dentro do container
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copiar todo o código da aplicação
COPY . /app/

# Expor a porta do Flask
EXPOSE 5000

# Comando para rodar o Flask
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=5000"]

