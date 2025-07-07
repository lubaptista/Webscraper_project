# Web Scraper - webscraper.io

> Projeto de estudo para aprender web scraping em Python de forma modular e profissional.

## 🎯 Objetivo

O scraper coleta dados de tabelas do site:

[https://webscraper.io/test-sites/tables](https://webscraper.io/test-sites/tables)

O objetivo é:
- entender scraping de listas e tabelas
- praticar BeautifulSoup
- estruturar scraping em módulos
- salvar dados em JSON e CSV
- escrever testes automatizados

---

## 🗂️ Estrutura do Projeto

webscraper_project/
├── config/
│   └── settings.py     → URLs, delays, user-agents
│
├── data/
│   ├── raw/
│   ├── processed/      → pasta onde o script guarda os dados processados ao final da execução
│   └── logs/
│
├── docs/
│   └── README.md
│
├── src/
│   ├── main.py         → orquestra o scraper
│   ├── scraper.py
│   ├── network.py      → requisições HTTP
│   ├── parser.py       → parse HTML (BeautifulSoup)
│   ├── extractor.py    → extrai dados das tabelas
│   ├── navigator.py    → lógica de paginação (neste site, vazio)
│   ├── storage.py      → salva JSON ou CSV
│   ├── utils.py        → funções genéricas
│   └── logger.py       → logging em arquivo
│
├── tests/              → testes unitários
│   ├── test_parser.py
│   ├── test_extractor.py
│   └── test_navigator.py
│
├── requirements.txt
└── .gitignore

---

## Tecnologias/Requisitos

- Python 3
- requests
- BeautifulSoup
- lxml

---

## 🚀 Instalação

Clone o repositório ou crie a pasta manualmente.

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Como Rodar

Execute o arquivo principal:
```bash
python -m src.main
```

Você verá algo assim no terminal:

```bash
Iniciando scraper do site webscraper.io/test-sites/tables ...
Scraping URL: https://webscraper.io/test-sites/tables
Coletadas 2 tabelas na página.
Scraping concluído!
```

E os arquivos serão salvos em:

```bash
data/processed/tables.json
data/processed/tables.csv

```