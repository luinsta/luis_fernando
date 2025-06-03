# 🧩 Projeto de Banco de Dados — Normalização & Modelagem Dimensional
## 🎯 Finalidade
Este projeto teve como meta transformar uma base de dados de locações inicialmente não normalizada em dois modelos distintos:
- Modelo Relacional Normalizado — seguindo até a 3ª Forma Normal.
- Modelo Dimensional — usando a técnica de Esquema Estrela para fins analíticos.

O objetivo foi garantir integridade, reduzir redundância e estruturar os dados para consultas eficientes.

# 🔍 Visão Geral das Etapas
## 📝 Etapa 1: Estudo da Estrutura Original
A base tb_locacao, fornecida como ponto de partida, agregava informações de diferentes entidades em uma única tabela:
- Dados pessoais dos clientes
- Especificações dos veículos (e tipo de combustível)
- Informações dos vendedores
- Registros de locação

Essa abordagem causava redundância e dificultava a manutenção dos dados (violando princípios de normalização).

## 🧹 Etapa 2: Aplicando Normalização (até 3FN)
Através da decomposição da tabela original, organizamos os dados em entidades independentes, com chaves primárias e estrangeiras bem definidas. Isso eliminou repetições e tornou o banco relacional mais coeso.

Foram criadas as seguintes tabelas:
- Cliente
- Carro
- Combustivel
- Vendedor
- Locacao

📜 Script SQL: modelo_normalizado.sql

## 📊 Etapa 3: Criação do Modelo Dimensional
Para análise de dados (BI), criamos um modelo baseado em Esquema Estrela, com foco em desempenho para consultas agregadas. Definimos uma fato central (FatoLocacao) e tabelas de dimensão:
- DimCliente
- DimCarro
- DimCombustivel
- DimVendedor
- DimTempo

📜 Script SQL: modelo_dimensional.sql

## 🗺️ Etapa 4: Representação Visual
Utilizamos o padrão PlantUML para desenhar os diagramas das estruturas criadas:

- Diagrama Entidade-Relacionamento do modelo normalizado
- Diagrama Estrela representando o modelo dimensional

📎 Acessíveis em:

- diagrama-modelo-relacional-normalizado.png
- diagrama-modelo-dimensional.png

⚙️ Tecnologias e Ferramentas Utilizadas
- SQLite: Análise preliminar da base original
- PostgreSQL + pgAdmin: Execução dos scripts e testes
- PlantUML: Geração dos diagramas
- VSCode: Edição dos scripts SQ

# 📁 Estrutura do Projeto
  📦 desafio-sprint
├── modelo_normalizado.sql
├── modelo_dimensional.sql
├── README.md
├── diagramas/
│   ├── diagrama-modelo-relacional-normalizado.png
│   ├── diagrama-modelo-dimensional.png
│   ├── codigo_diagrama_normalizado.puml
│   └── codigo_diagrama_dimensional.puml
└── evidencias/
    ├── 00_execucao_modelo_base.png
    ├── 01_tabelas_criadas_normalizado.png
    ├── 02_tabelas_criadas_dimensional.png
    ├── 03_insercao_dados_teste.png
    ├── 04_visualizacao_dados.png
    ├── 05_criacao_diagrama_normalizado.png
    └── 06_criacao_diagrama_dimensional.png

