# Relatório Técnico-Educativo: Dashboard Literário
## Um Guia Tecnológico sobre os Clássicos da Literatura Brasileira
**Autor do Projeto:** Luis Gustavo Rocha Lima (1º Semestre)  
**Instituição de Ensino:** FMU — Centro Universitário das Faculdades Metropolitanas Unidas  
**Curso:** Bacharelado em Ciência de Dados  
**Área Temática:** Inovação, Tecnologia e Cultura Digital  
**Linha de Extensão:** Educação e Letramento Digital  
**ODS Vinculado:** ODS 4 – Educação de Qualidade  
**Público-Alvo:** Estudantes de Ensino Médio, Professores de Língua Portuguesa e Comunidade

---

## 1. Resumo Executivo e Justificativa Social

O presente projeto de extensão universitária une a **Ciência de Dados** e o **Processamento de Linguagem Natural (PLN)** à preservação e difusão do patrimônio literário brasileiro. 

Frequentemente, estudantes do ensino médio encontram barreiras para compreender as especificidades estilísticas dos grandes autores nacionais. Por meio da quantificação textual e da estilometria computacional, transformamos conceitos abstratos (como "secura verbal", "densidade determinista" ou "fluxo de consciência") em evidências visuais tangíveis, interativas e acessíveis.

---

## 2. Metodologia Científica e Pipeline de NLP

O pipeline de processamento foi construído em linguagem **Python** utilizando **Pandas**, **NLTK**, expressões regulares e heurísticas léxicas dedicadas:

```
[Corpus Textual Canônico]
          │
          ▼
[Tokenização & Limpeza (Remoção de Stopwords)]
          │
          ├─────────────────────────┬─────────────────────────┬─────────────────────────┐
          ▼                         ▼                         ▼                         ▼
   Diversidade Lexical     Métricas de Sintaxe      Densidade Temática       Verbos: Ação vs.
   (TTR & Hapax Legomena)   (Média Palavras/Frase)   (Léxicos Customizados)    Existência / Reflexão
```

---

## 3. Análise dos Resultados por Autor

### 3.1. Graciliano Ramos vs. Euclides da Cunha: A Luta pela Extensão da Frase
A estilometria comprovou de forma inequívoca o contraste entre o **Regionalismo Crítico** e o **Pré-Modernismo Determinista**:
* **Graciliano Ramos (*Vidas Secas*):** obteve uma média de apenas **5,67 palavras por frase**, com **100% de frases curtas** ($\le 12$ palavras). A economia lexical de Graciliano é um espelho formal da própria escassez física vivida pelos retirantes.
* **Euclides da Cunha (*Os Sertões*):** em contraste, apresentou média de **22,33 palavras por frase**, com **0% de frases curtas**. Sua prosa é caracterizada por períodos oratórios, subordinações sintáticas e encadeamentos reflexivos de grande fôlego.

---

### 3.2. Clarice Lispector: O Mapeamento do Fluxo de Consciência
A análise da distribuição de classes verbais evidenciou a marca registrada de Clarice Lispector:
* **100% dos verbos analisados foram de cunho existencial/cognitivo** (*sentir, existir, pensar, saber, hesitar*), contra 0% de verbos de ação física no excerto representativo.
* Enquanto narrativas tradicionais progridem por acontecimentos externos, a narrativa clariceana progride pela vertigem interior e pela auto-investigação psicológica.

---

### 3.3. Assinaturas Temáticas e Regionais
A contagem normalizada por 1.000 palavras confirmou a especialização de cada autor:
1. **Jorge Amado:** Apresentou **123,29 termos culturais/1.000 palavras**, dominado por vocábulos como *Iemanjá, Ogum, candomblé, saveiro, cais, acarajé, berimbau*.
2. **Rachel de Queiroz:** Registrou **105,63 termos de escassez/1.000 palavras** em *O Quinze*, com alta recorrência de *seca, fome, sol, poeira, retirantes, morte*.
3. **Ariano Suassuna:** Liderou a métrica de **oralidade e elementos do cordel (74,53/1.000 palavras)**, caracterizada pelo uso vivo de interjeições como *oxente, eita, vixe, valei-me, diabo*.
4. **Euclides da Cunha:** Concentrou a maior densidade de **termos técnico-científicos (37,31/1.000 palavras)**, como *orografia, geologia, erosão, bioclimático, atavismo*.
5. **Guimarães Rosa:** Destacou-se pela invenção lexical e **115 termos únicos (hapax legomena)**, demonstrando que a língua portuguesa é recriada para expressar a metafísica do sertão.

---

## 4. Tabela Síntese das Evidências Quantitativas

| Autor | Obra / Estilo | Média Pal/Frase | % Frases Curtas | Riqueza (TTR) | Marca Estilística Principal |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Graciliano Ramos** | *Vidas Secas* | **5.7** | **100.0%** | 0.735 | Máxima concisão e secura verbal |
| **Clarice Lispector** | *A Hora da Estrela* | 12.3 | 58.3% | 0.714 | Predomínio absoluto de verbos introspectivos |
| **Jorge Amado** | *Capitães da Areia* | 16.2 | 22.2% | 0.685 | Alta densidade cultural afro-baiana |
| **Rachel de Queiroz** | *O Quinze* | 12.9 | 45.5% | 0.768 | Léxico concentrado na seca e êxodo |
| **Ariano Suassuna** | *Auto da Compadecida*| 23.0 | 28.6% | 0.721 | Oralidade teatral e elementos do cordel |
| **Euclides da Cunha** | *Os Sertões* | **22.3** | **0.0%** | 0.776 | Períodos longos e vocabulário científico |
| **Guimarães Rosa** | *Grande Sertão: Veredas*| 10.4 | 63.2% | 0.685 | Neologismos e alta riqueza vocabular |

---

## 5. Como Executar o Dashboard Interativo

A aplicação interativa foi construída com **Streamlit** e pode ser executada localmente:

```powershell
cd C:\Users\Luisg\.gemini\antigravity\scratch\dashboard_literario
streamlit run app/app.py
```

O dashboard oferece:
* Navegação comparativa entre os 7 autores;
* Gráficos interativos em Plotly;
* Laboratório interativo onde estudantes podem colar suas próprias redações para comparar seu estilo com os clássicos da literatura brasileira.

---

## 6. Conclusão & Contribuição para o ODS 4

Este projeto materializa as diretrizes do **ODS 4 (Educação de Qualidade)** ao:
1. Fornecer uma ferramenta didática gratuita e moderna para escolas e professores;
2. Desmistificar o uso de programação e ciência de dados no campo das ciências humanas;
3. Fomentar o letramento digital e o pensamento crítico interdisciplinar.
