FROM python:3.12-slim

# Atualize os pacotes e instale as dependências necessárias
RUN apt-get update && \
    apt-get install -y build-essential cmake libboost-all-dev libssl-dev libffi-dev python3-dev && \
    apt-get install -y --no-install-recommends gfortran libopenblas-dev liblapack-dev && \
    apt-get install -y pkg-config libmariadb-dev-compat libmariadb-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho
WORKDIR /app

# Copie o seu código para o contêiner
COPY . /app

# Instale as dependências do Python
RUN pip install --no-cache-dir cmake
RUN pip install --no-cache-dir pyarrow mysqlclient
RUN pip install --no-cache-dir -r requirements.txt

# Comando para executar o aplicativo
CMD ["streamlit", "run", "Home.py"]
