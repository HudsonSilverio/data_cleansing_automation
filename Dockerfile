# Usando uma imagem oficial do Python leve
FROM python:3.12.1-slim

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar arquivos do projeto para dentro do container
COPY . /app

# Atualizar pacotes do sistema e instalar dependências essenciais
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# Instalar Poetry para gerenciar as dependências do projeto
RUN pip install --no-cache-dir poetry

# Configurar Poetry para não criar ambiente virtual dentro do container
RUN poetry config virtualenvs.create false

# Instalar todas as dependências do projeto
RUN poetry install --no-root --no-interaction --no-ansi

# Criar diretórios necessários e garantir permissões corretas
RUN mkdir -p /app/uploads /app/processed && chmod -R 777 /app/uploads /app/processed

# Expor a porta 5000 (onde o Flask será executado)
EXPOSE 5000

# Definir a variável de ambiente do Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV PYTHONUNBUFFERED=1

# Usar Gunicorn para rodar o Flask em produção com 4 workers
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]


