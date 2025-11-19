# 📊 DIO & Santander 2025 — Pipeline ETL com IA Generativa  
### Python • Groq • Railway • Jupyter Notebook

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-IA%20Generativa-purple?logo=openai&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-Deploy-black?logo=railway&logoColor=white)
![ETL](https://img.shields.io/badge/ETL-Pipeline-green)
![Status](https://img.shields.io/badge/Status-Concluído-success)


## 📘 Visão Geral

Este repositório contém um **pipeline ETL completo** desenvolvido para o **Desafio Santander 2025 (DIO)**, integrando:

- Dados reais consumidos de uma API hospedada no **Railway**  
- IA generativa utilizando a **Groq API**  
- Processamento e atualização de registros via **Python**

O pipeline foi implementado tanto em **Jupyter Notebook** quanto em **script Python**, permitindo flexibilidade nos testes e execuções.

---

## 🚀 Objetivo do Projeto

Você assume o papel de um cientista de dados responsável por:

1. **Extrair** IDs de usuários de um CSV  
2. **Consultar** dados completos na API  
3. **Gerar mensagens personalizadas** usando IA generativa (Groq)  
4. **Atualizar** o cliente na API, adicionando a nova mensagem  

Todo o processo funciona de ponta a ponta.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Função |
|-----------|--------|
| 🐍 **Python** | Implementação do ETL |
| 📒 **Jupyter Notebook** | Desenvolvimento inicial do pipeline |
| 🤖 **Groq API** | IA generativa para personalização |
| 🧮 **Pandas** | Manipulação de dados |
| 🌐 **Requests** | Consumo da API |
| 🚀 **Railway** | Deploy da API usada no pipeline |
| 🔧 **Procfile** | Configuração do deploy |
| 📦 **GitHub** | Versionamento e portfólio |

---

## 📁 Estrutura do Repositório

```text
📦 siqueiradelimarafaella-boop
├── Procfile                    # Arquivo usado pelo Railway para deploy
├── requirements.txt            # Dependências do projeto
│
├── SD2025.csv                  # IDs dos usuários
│
├── Santander2025_2.ipynb       # Notebook com o pipeline completo
├── santander2025_2.py          # Versão Python do pipeline
├── main.py                     # Arquivo usado no deploy
│
└── README.md                   # Este arquivo

```


---

## ✨ Autora

**Rafaella Siqueira**  
Projeto criado como parte do desafio **DIO & Santander 2025 — Explorando IA Generativa em um Pipeline de ETL**.

