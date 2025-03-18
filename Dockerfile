# Usa uma imagem baseada no Debian
FROM python:3.12.1-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia primeiro o requirements.txt para evitar rebaixamento do cache
COPY requirements.txt .

# Instala dependências do Python
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copia os demais arquivos do projeto
COPY . .

# Comando para iniciar a aplicação (ajuste se necessário)
CMD ["python", "app.py"]




