# Análise de Dados com Python

Este projeto realiza a análise de dados de vendas utilizando Python e bibliotecas populares como Pandas, Matplotlib e Seaborn.

## Estrutura do Projeto

analise-dados/
│
├── data/
│   └── vendas.csv
│
├── src/
│   └── analise_vendas.py
│
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/analise-dados.git
   cd analise-dados

2.  Construa a imagem Docker:
    docker build -t analise-dados .

3.  Execute o contêiner Docker:
    docker run -v $(pwd)/data:/app/data analise-dados