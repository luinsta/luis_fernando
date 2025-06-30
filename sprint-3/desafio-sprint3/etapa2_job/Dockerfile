# Dockerfile para a Etapa 2: Análise e Gráficos (job.py)

# Etapa 1: Imagem Base
FROM python:3.10-slim

# Etapa 2: Diretório de Trabalho
WORKDIR /app

# Etapa 3: Copiar e Instalar Dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 4: Copiar Arquivo da Aplicação
COPY job.py .

# Etapa 5: Comando de Execução
CMD ["python", "job.py"]