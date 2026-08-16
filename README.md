# Spotify Streaming History Analytics

Pipeline de dados End-to-End desenvolvido para extrair, transformar, armazenar e visualizar o histórico pessoal de reproduções do Spotify. O projeto abrange desde a ingestão de dados brutos em formato JSON via Python até a estruturação de um banco de dados relacional e a criação de um dashboard executivo interativo no Power BI.

---

## Visao Geral do Dashboard

![Visualizacao do Dashboard]([docs/dashboard_preview.png](https://github.com/nicolas-oliveiradev/spotify-streaming-analytics/blob/main/docs/dashboard_spotify.png))

---

## Arquitetura da Solucao e Tecnologias

* **Ingestao e Tratamento de Dados (Python / Pandas):**
  * Leitura e consolidacao dos arquivos JSON brutos do historico de reproducao.
  * Tratamento de valores ausentes, conversao de tipos de dados e transformacao de milissegundos para minutos e horas.

* **Armazenamento Relacional (SQLite):**
  * Carga dos dados limpos em banco de dados relacional.
  * Consultas SQL para validacao de integridade e regras de negocio.

* **Visualizacao e Business Intelligence (Power BI / DAX):**
  * Modelagem de dados e criacao de medidas dinamicas em DAX.
  * Interface desenvolvida em Dark Mode, priorizando usabilidade (UX/UI) e hierarquia de informacoes.

---

## Principais Metricas e Insights

* **Volume Total:** Mais de 803 horas de reproducao acumuladas em aproximadamente 15 mil execucoes.
* **Artista Mais Ouvido:** Lideranca do artista YOASOBI, superando 100 horas de execucao no periodo.
* **Consumo Diario:** Média ajustada de aproximadamente 66 minutos diarios.
* **Tendencia:** Crescimento continuo no volume de reproducoes a partir de novembro de 2025.

---

## Medidas DAX Principais

### 1. Artista Mais Ouvido

```dax
Artista_Mais_Ouvido = 
TOPN(
    1, 
    VALUES(spotify_limpo[artista]), 
    CALCULATE(SUM(spotify_limpo[tempo_horas])), 
    DESC
)
```
### 2. Média de Minutos Diários

```dax
Media_Minutos_Diarios = 
DIVIDE(
    SUM(spotify_limpo[tempo_minutos]),
    CALCULATE(
        DISTINCTCOUNT(spotify_limpo[data_reproducao].[Data])
    )
)
```

├── data/
│   ├── raw/              # Arquivos JSON brutos do Spotify
│   └── processed/        # Banco SQLite com os dados limpos
├── scripts/
│   ├── etl_spotify.py    # Script Python de extracao e tratamento
│   └── queries.sql       # Consultas SQL para validacao
├── dashboard/
│   └── spotify_analytics.pbix  # Arquivo principal do Power BI
├── docs/
│   └── dashboard_preview.png   # Imagem do dashboard para o README
└── README.md             # Documentacao do projeto

## Como Executar o Projeto
### 1. Clonar o repositorio:

git clone [https://github.com/seu-usuario/spotify-streaming-analytics.git](https://github.com/seu-usuario/spotify-streaming-analytics.git)

### 2. Executar a ETL em Python:

python scripts/etl_spotify.py

### 3. Abrir o Dashboard:

Abra o arquivo dashboard/spotify_analytics.pbix no Power BI Desktop.

Atualize a conexao do banco apontando para o arquivo SQLite em data/processed/.

## Autor
Desenvolvido por Nicolas Oliveira Araujo.

LinkedIn: [link-do-perfil](https://www.linkedin.com/in/nicolas-oliveira-araújo-b8a40133b/)

GitHub: [link-do-github](https://github.com/nicolas-oliveiradev)
