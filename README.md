# 📚 Dashboard Literário: Um Guia Tecnológico sobre os Clássicos da Literatura Brasileira

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![ODS 4](https://img.shields.io/badge/ODS%204-Educa%C3%A7%C3%A3o%20de%20Qualidade-C5192D.svg)](https://brasil.un.org/pt-br/sdgs/4)
[![Instituição](https://img.shields.io/badge/FMU-Ci%C3%AAncia%20de%20Dados-8B3A42.svg)](https://fmu.br/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Atividade Curricular de Extensão (ACE) em Ciência de Dados**  
> **Autor:** **Luis Gustavo Rocha Lima** (1º Semestre)  
> **Instituição:** FMU — Centro Universitário das Faculdades Metropolitanas Unidas  
> **Objetivo de Desenvolvimento Sustentável:** **ODS 4 – Educação de Qualidade (UNESCO/ONU)**  
> **Área Temática:** Inovação, Tecnologia e Cultura Digital | Educação e Letramento Digital  

---

## 📖 Sobre o Projeto

O **Dashboard Literário** une a **Ciência de Dados** e o **Processamento de Linguagem Natural (PLN)** à valorização e democratização dos grandes clássicos da literatura brasileira. 

Utilizando técnicas de estilometria computacional, o projeto comprova e ilustra visualmente as escolhas estilísticas de **7 autores canônicos nacionais**, tornando conceitos literários abstratos (como a "secura verbal" de Graciliano Ramos ou a "densidade científica" de Euclides da Cunha) em evidências quantitativas e didáticas acessíveis para estudantes e professores do ensino básico.

---

## 🎯 Escopo dos Autores Analisados

| Autor | Obra Canônica | Foco da Análise Computacional | Métrica Principal Identificada |
| :--- | :--- | :--- | :---: |
| **Graciliano Ramos** | *Vidas Secas* | Concisão, economia vocabular e frases curtas | **5,7 palavras/frase** (100% frases curtas) |
| **Euclides da Cunha** | *Os Sertões* | Linguagem científica determinista vs. epopeia sertaneja | **22,3 palavras/frase** (37,3 termos técnicos/1k) |
| **Clarice Lispector** | *A Hora da Estrela* | Fluxo de consciência e verbos reflexivos vs. ação | **100% verbos existenciais/cognitivos** |
| **Guimarães Rosa** | *Grande Sertão: Veredas* | Invenção neológica e riqueza vocabular | **115 Hapax Legomena** (termos únicos) |
| **Jorge Amado** | *Capitães da Areia* | Identidade cultural baiana, orixás e sincretismo | **123,3 ocorrências/1k** no campo afro-baiano |
| **Rachel de Queiroz** | *O Quinze* | Léxico da seca, fome, escassez e êxodo | **105,6 ocorrências/1k** no campo da seca |
| **Ariano Suassuna** | *Auto da Compadecida* | Oralidade, interjeições e elementos do cordel | **74,5 ocorrências/1k** de oralidade e cordel |

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com/SEU-USUARIO/dashboard-literario.git
cd dashboard-literario
```

### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 3. Executar o Web Dashboard Interativo (Figma UI & Animações)
O dashboard web com visual editorial e interações de hover pode ser aberto diretamente ou servido localmente:
```bash
# Servir via Python HTTP Server na porta 3000
python -m http.server 3000 --directory app/web
```
Acesse no seu navegador: **`http://localhost:3000`**

### 4. Executar o Dashboard Streamlit (Alternativo)
```bash
streamlit run app/app.py
```
Acesse no seu navegador: **`http://localhost:8501`**

---

## 📁 Estrutura de Diretórios

```
dashboard_literario/
├── app/
│   ├── app.py                     # Aplicação interativa em Streamlit
│   └── web/                       # Web Dashboard estilizado (Figma)
│       ├── index.html             # Interface interativa, animações e laboratório de NLP
│       └── assets/authors/        # Retratos canônicos em alta resolução
├── src/
│   ├── nlp_analyzer.py            # Motor de NLP: TTR, sintaxe, léxicos temáticos
│   ├── corpus_data.py             # Corpus literário canônico e metadados pedagógicos
│   └── generate_visualizations.py # Gerador de gráficos estatísticos (Matplotlib/Seaborn)
├── reports/
│   ├── relatorio_educativo.html   # Relatório oficial didático pronto para impressão/PDF
│   ├── relatorio_educativo.md     # Documento em Markdown
│   └── figures/                   # Gráficos de alta resolução para divulgação
├── data_summary.csv               # Tabela consolidada com todas as métricas extraídas
├── requirements.txt               # Dependências do ecossistema Python
└── README.md                      # Apresentação do projeto e instruções
```

---

## 🖨️ Produto Comunitário (Entrega de Extensão)

O projeto disponibiliza um **Relatório Técnico-Educativo** completo pronto para uso em sala de aula e divulgação comunitária em:
* [`reports/relatorio_educativo.html`](reports/relatorio_educativo.html) *(abra no navegador e aperte `Ctrl + P` para gerar o PDF institucional com formatação diagramada)*.

---

## 👨‍💻 Autor & Agradecimentos

* **Luis Gustavo Rocha Lima**
* **1º Semestre** · Bacharelado em Ciência de Dados
* **FMU — Centro Universitário das Faculdades Metropolitanas Unidas**
* Alinhado aos princípios do **ODS 4 – Educação de Qualidade**
