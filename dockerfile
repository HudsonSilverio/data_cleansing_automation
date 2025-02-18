# Usando a imagem do Python 3.12.1
FROM python:3.12.1

# Instalando o Poetry
RUN pip install poetry

# Copiando o código fonte para o diretório /src
COPY . /src

# Definindo o diretório de trabalho
WORKDIR /src

# Instalando as dependências do Poetry
RUN poetry install --no-root

# Definir o comando de inicialização para um shell interativo (sem rodar o código)
ENTRYPOINT ["bash"]
