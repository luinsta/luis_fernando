# Dockerfile para a Etapa 1: ETL (etl.py)

# Etapa 1: Imagem Base
FROM python:3.10-slim

# Etapa 2: Diretório de Trabalho
WORKDIR /app

# Etapa 3: Copiar e Instalar Dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 4: Copiar Arquivos da Aplicação
COPY etl.py .
COPY concert_tours_by_women.csv .

# Etapa 5: Comando de Execução
CMD ["python", "etl.py"]