# Pipeline de Dados com Docker: Análise de Turnês Musicais

## Sobre Este Projeto

Este repositório contém a solução para um desafio prático de engenharia de dados. O projeto consiste em um pipeline totalmente automatizado que processa um conjunto de dados brutos sobre as turnês mais lucrativas de artistas femininas, realizando o ciclo completo de vida dos dados: desde a limpeza inicial até a análise e geração de relatórios visuais.

A principal característica deste projeto é que todo o fluxo de trabalho é **containerizado e orquestrado com Docker e Docker Compose**, o que garante portabilidade, consistência e uma execução simplificada em qualquer ambiente.

O pipeline foi projetado para:

  * **Extrair, Transformar e Carregar (ETL):** Ler dados brutos de um arquivo `.csv`, tratar inconsistências, limpar valores e criar novas features para análise.
  * **Analisar e Visualizar Dados:** Consumir os dados tratados para responder a perguntas de negócio e gerar saídas claras, como relatórios em texto e gráficos.
  * **Automatizar com Containers:** Orquestrar a execução sequencial das etapas de ETL e análise, garantindo que o fluxo de dados seja coeso e à prova de falhas.

## O Pipeline: Passo a Passo

O processo é dividido em dois estágios independentes, cada um rodando em seu próprio container, que se comunicam através de um volume de dados compartilhado.

#### `Estágio 1: Limpeza e Transformação (ETL)`

O primeiro container é responsável por executar o script `etl.py`, que realiza o trabalho de preparação dos dados. As principais tarefas são:

  * **Carregar** o dataset `concert_tours_by_women.csv`.
  * **Corrigir** inconsistências nos nomes das colunas (ex: `Adjustedgross` para `Adjusted gross`).
  * **Transformar** a coluna `Year(s)` (ex: "2008-2009") em duas colunas numéricas: `Start year` e `End year`.
  * **Limpar** os dados monetários, removendo símbolos como `$` e `,` para permitir cálculos.
  * **Recalcular** o `Rank` das turnês com base nos dados limpos e ordenados.
  * **Exportar** o resultado final como `csv_limpo.csv` no volume compartilhado.

#### `Estágio 2: Análise e Geração de Insights`

Após a conclusão bem-sucedida do primeiro estágio, o segundo container é iniciado. Ele executa o script `job.py`, que:

  * **Consome** o `csv_limpo.csv` do volume compartilhado.
  * **Executa análises** com a biblioteca Pandas para responder a 5 questões de negócio.
  * **Gera os entregáveis finais:**
      * Um arquivo `respostas.txt` contendo as respostas diretas.
      * Dois gráficos (`Q4.png` e `Q5.png`) para visualização de dados.

## Tecnologias e Ferramentas

  * **Linguagem:** Python 3
  * **Análise de Dados:** Pandas, NumPy
  * **Visualização de Dados:** Matplotlib, Seaborn
  * **Containerização e Orquestração:** Docker, Docker Compose

## Arquitetura do Projeto

O repositório foi organizado em módulos para refletir os estágios do pipeline, mantendo uma clara separação de responsabilidades:

```
desafio-sprint3/
├── etapa1_etl/
│   ├── concert_tours_by_women.csv    # Dataset de entrada (bruto)
│   ├── etl.py                        # Script com a lógica de ETL
│   ├── requirements.txt              # Dependências do Python para o ETL
│   └── Dockerfile                    # Receita para construir o container de ETL
│
├── etapa2_job/
│   ├── job.py                        # Script com a lógica de análise
│   ├── requirements.txt              # Dependências do Python para o Job
│   └── Dockerfile                    # Receita para construir o container de análise
│
├── volume/                           # Diretório para os dados de saída (criado/populado na execução)
│
├── docker-compose.yaml               # Arquivo principal de orquestração
└── README.md                         # Esta documentação
```

## Guia de Execução Rápida

#### Requisitos

Apenas uma instalação funcional do **Docker Desktop** é necessária para executar o projeto.

#### Passos para Execução

1.  **Clone o Repositório**
    ```bash
    git clone https://github.com/desktop/desktop/issues/18661
    ```
2.  **Acesse o Diretório do Projeto**
    ```bash
    cd desafio-sprint3
    ```
3.  **Execute o Pipeline**
    Este único comando constrói as imagens e executa todo o pipeline de forma automatizada:
    ```bash
    docker-compose up --build
    ```

## Resultados e Entregáveis

Após a execução do comando, a pasta `volume/` será populada com os seguintes arquivos:

  * `csv_limpo.csv`: A base de dados tratada, pronta para ser consumida.
  * `respostas.txt`: As respostas em texto para as perguntas de 1 a 3.
  * `Q4.png`: Gráfico de linhas mostrando a evolução do faturamento por ano da artista em destaque.
  * `Q5.png`: Gráfico de barras com o top 5 artistas por número de shows.

