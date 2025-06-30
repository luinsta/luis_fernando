# Resumo da Sprint

## Visão Geral

Esta sprint de desenvolvimento teve como foco a imersão em três pilares essenciais da tecnologia atual: **Containerização de Aplicações com Docker**, **Estratégias de Cloud Computing na AWS** e **Processamento de Dados com Python e Expressões Regulares (REGEX)**. O objetivo foi consolidar a base teórica e aplicá-la diretamente em um desafio prático de ponta a ponta.

---

## Focos de Aprendizado

### 1. Ecossistema Docker para Desenvolvedores

Aprofundamento no universo Docker, desde a criação de imagens e gerenciamento de containers até a orquestração de aplicações complexas em ambientes de produção.

**Tópicos Centrais:**
- **Desenvolvimento de `Dockerfile`:** Aplicação de boas práticas para criar imagens otimizadas, seguras e eficientes.
- **Persistência de Dados com `Volumes`:** Estratégias para gerenciar dados de estado em aplicações containerizadas.
- **Conectividade e Redes:** Configuração da comunicação entre múltiplos containers e exposição de serviços para o exterior.
- **Automação com `Docker Compose`:** Orquestração de ambientes de desenvolvimento e produção com múltiplos serviços interligados.
- **Visão de Orquestração em Escala:** Introdução aos paradigmas de gerenciamento de clusters com **Docker Swarm** e **Kubernetes (K8s)**, compreendendo os fundamentos para criar aplicações distribuídas e de alta disponibilidade.

### 2. AWS Partner: Acreditação Técnica

Treinamento técnico e de negócios voltado para o ecossistema de parceiros da AWS, com o objetivo de alinhar o conhecimento dos serviços à capacidade de apresentar soluções de valor para os clientes.

**Tópicos Centrais:**
- **Benefícios Estratégicos da Nuvem:** Análise da proposta de valor da AWS em termos de agilidade, elasticidade, redução de custos e alcance global.
- **Core Services da AWS:** Fundamentos dos serviços essenciais da nuvem da Amazon, como EC2, S3, RDS e VPC.
- **Articulação de Valor e Negócios:** Técnicas para comunicar os benefícios técnicos em linguagem de negócios e superar objeções comuns.
- **Go-to-Market com a AWS:** Estratégias para construir e comercializar soluções em parceria com a AWS.


### 3. Expressões Regulares (REGEX) com Python

Domínio prático de Expressões Regulares (REGEX) aplicadas em Python, uma ferramenta essencial para a manipulação e extração de dados textuais de forma precisa e eficiente.

**Tópicos Centrais:**
- **Fundamentos da Sintaxe REGEX:** Domínio dos metacaracteres e da lógica para a construção de padrões de busca.
- **Implementação com o Módulo `re`:** Uso prático das funções `search()`, `match()`, `findall()` e `sub()` do Python para interagir com textos.
- **Aplicações Práticas:** Uso de REGEX em cenários reais, como limpeza de dados (data cleaning), validação de formatos (CPF, e-mail) e extração de informações estruturadas de textos não estruturados.

---

## Desafio Prático: Construção de um Pipeline de Dados

A consolidação de todo o aprendizado se deu através de um desafio prático: a construção de um pipeline de dados completo, orquestrado de ponta a ponta com Docker Compose.

- **Estágio de ETL (Extração, Transformação e Carga):** O primeiro container foi encarregado de ingerir um dataset bruto, executar a limpeza de dados, padronizar colunas e transformar informações (como extrair múltiplos anos de uma única string de texto).
- **Estágio de Análise (Job):** O segundo container, acionado após o sucesso do primeiro, utilizou os dados já tratados para realizar análises com Pandas, resultando em um relatório em texto e em visualizações gráficas.

Este exercício foi fundamental para solidificar na prática os conceitos de `Dockerfile`, `Docker Compose` e `Volumes`, simulando um ambiente de trabalho real.

---

## Principais Competências Desenvolvidas

- **Arquitetura de Microsserviços e Containers:** Capacidade de projetar, construir e orquestrar aplicações baseadas em containers com Docker e Docker Compose, com uma base conceitual para operar em escala com Kubernetes.
- **Visão de Negócios em Nuvem (AWS):** Habilidade de conectar soluções técnicas na AWS com os objetivos de negócio de um cliente, entendendo o ecossistema de parceiros e os serviços fundamentais.
- **Engenharia de Dados e Análise com Python:** Proficiência em todo o ciclo de vida de um projeto de dados, desde a limpeza e transformação com Pandas até a extração de insights e a habilidade de usar REGEX para tarefas complexas.
- **Práticas de Automação e DevOps:** Aplicação prática de uma mentalidade DevOps, utilizando a containerização para criar pipelines de software consistentes, automatizados e independentes de ambiente.
