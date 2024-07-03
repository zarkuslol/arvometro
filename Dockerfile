# Usar uma imagem base de Python
FROM python:3.9-slim

# Instalar dependências necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    libmysqlclient-dev

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de requisitos e instalar dependências do Python
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o conteúdo do projeto para o diretório de trabalho
COPY . .

# Expor a porta usada pelo Streamlit
EXPOSE 82

# Comando para rodar a aplicação
CMD ["streamlit", "run", "utils/Home.py"]
