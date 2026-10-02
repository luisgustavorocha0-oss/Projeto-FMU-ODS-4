"""
Dashboard Literário: Um Guia Tecnológico sobre os Clássicos da Literatura Brasileira
Aplicação Streamlit interativa para Educação e Letramento Digital (ODS 4).
"""
import sys
from pathlib import Path

# Add project root to Python module search path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.corpus_data import AUTHORS_METADATA, CORPUS_TEXTS
from src.nlp_analyzer import analyze_author_text, tokenize_words, compute_lexical_diversity

st.set_page_config(
    page_title="Dashboard Literário | Clássicos Brasileiros",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.3rem;
        font-weight: 800;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #475569;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #F8FAFC;
        border-radius: 10px;
        padding: 1.2rem;
        border-left: 5px solid #3B82F6;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
    .quote-box {
        background-color: #FEF3C7;
        border-left: 5px solid #F59E0B;
        padding: 1rem;
        border-radius: 8px;
        font-style: italic;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-title">📚 Dashboard Literário: Clássicos Brasileiros</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title"><b>Ciência de Dados aplicada à Literatura & Educação (ODS 4)</b> | Processamento de Linguagem Natural & Estilometria</div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://images.unsplash.com/photo-1457369804613-52c61a468e7d?auto=format&fit=crop&w=400&q=80", use_container_width=True)
st.sidebar.title("Navegação Didática")

menu = st.sidebar.radio(
    "Selecione o Módulo:",
    ["📊 Visão Geral Comparativa", 
     "🔍 Análise Individual por Autor", 
     "🧪 Laboratório de NLP (Teste seu Texto)",
     "📖 Sobre o Projeto & Metodologia (ODS 4)"]
)

# Load data
@st.cache_data
def get_author_data():
    data = []
    for key, text in CORPUS_TEXTS.items():
        meta = AUTHORS_METADATA[key]
        profile = analyze_author_text(text, key)
        data.append({
            "key": key,
            "name": meta["name"],
            "movement": meta["movement"],
            "target": meta["analysis_target"],
            "quote": meta["iconic_quote"],
            "hypothesis": meta["hypothesis"],
            "tokens": profile["tokens_count"],
            "sentences": profile["sentences_count"],
            "ttr": profile["lexical_diversity"]["ttr"],
            "hapax": profile["lexical_diversity"]["hapax_legomena"],
            "hapax_ratio": profile["lexical_diversity"]["hapax_ratio"],
            "avg_words_sent": profile["sentence_metrics"]["avg_words_per_sentence"],
            "short_sent_pct": profile["sentence_metrics"]["short_sentences_ratio"] * 100,
            "refl_ratio": profile["reflection_vs_action"]["reflection_ratio"] * 100,
            "seca_density": profile["thematic_densities"]["secura_escassez"]["density_per_1k"],
            "bahia_density": profile["thematic_densities"]["cultura_baiana"]["density_per_1k"],
            "ciencia_density": profile["thematic_densities"]["cientifico_determinista"]["density_per_1k"],
            "cordel_density": profile["thematic_densities"]["oralidade_cordel"]["density_per_1k"],
            "top_words": profile["top_content_words"]
        })
    return pd.DataFrame(data)

df = get_author_data()

# ==============================================================================
# MÓDULO 1: VISÃO GERAL COMPARATIVA
# ==============================================================================
if menu == "📊 Visão Geral Comparativa":
    st.subheader("Panorama Comparativo dos 7 Clássicos")
    st.info("💡 **Objetivo Pedagógico:** Demonstrar como os números revelam a impressão digital estilística de cada autor — desde a 'secura' de Graciliano até a erudição científica de Euclides da Cunha.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Mais Conciso (Frases Curtas)", "Graciliano Ramos", "5.7 pal/frase")
    with col2:
        st.metric("Maior Período Sintático", "Euclides da Cunha", "22.3 pal/frase")
    with col3:
        st.metric("Mais Introspectiva", "Clarice Lispector", "100% Reflexão")
    with col4:
        st.metric("Maior Vocabulário Único", "Guimarães Rosa", "115 Hapax")
        
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["📏 Sintaxe & Concisão", "🎨 Assinaturas Temáticas", "🧠 Fluxo de Consciência"])
    
    with tab1:
        st.markdown("### Comprimento Médio de Sentenças (Palavras por Frase)")
        st.caption("Graciliano Ramos economiza palavras (estilo despojado), enquanto Euclides constrói períodos complexos de ensaio científico.")
        
        fig_sent = px.bar(
            df.sort_values(by="avg_words_sent"),
            x="name",
            y="avg_words_sent",
            color="avg_words_sent",
            color_continuous_scale="Blues",
            labels={"avg_words_sent": "Média de Palavras / Frase", "name": "Autor"},
            text_auto=".1f"
        )
        fig_sent.update_layout(xaxis_tickangle=-25, showlegend=False, height=450)
        st.plotly_chart(fig_sent, use_container_width=True)

    with tab2:
        st.markdown("### Densidade de Campos Semânticos (por 1.000 palavras)")
        st.caption("Cada autor projeta seu universo: Amado na cultura baiana, Rachel no drama da seca, Euclides na ciência.")
        
        thematic_df = df.melt(
            id_vars=["name"],
            value_vars=["seca_density", "bahia_density", "ciencia_density", "cordel_density"],
            var_name="Campo Temático",
            value_name="Densidade"
        )
        thematic_df["Campo Temático"] = thematic_df["Campo Temático"].map({
            "seca_density": "Seca & Escassez",
            "bahia_density": "Cultura Baiana",
            "ciencia_density": "Termos Científicos",
            "cordel_density": "Oralidade / Cordel"
        })
        
        fig_theme = px.bar(
            thematic_df,
            x="name",
            y="Densidade",
            color="Campo Temático",
            barmode="group",
            labels={"name": "Autor", "Densidade": "Ocorrências / 1.000 palavras"}
        )
        fig_theme.update_layout(xaxis_tickangle=-25, height=480)
        st.plotly_chart(fig_theme, use_container_width=True)

    with tab3:
        st.markdown("### Índice de Introspecção: Verbos Reflexivos vs. Ação")
        st.caption("Proporção de verbos de cognição/sentir (*pensar, sentir, ser, parecer*) contra verbos de ação física (*correr, bater, fugir*).")
        
        fig_refl = px.bar(
            df.sort_values(by="refl_ratio", ascending=False),
            x="name",
            y="refl_ratio",
            color="refl_ratio",
            color_continuous_scale="Purples",
            labels={"refl_ratio": "Índice Introspectivo (%)", "name": "Autor"},
            text_auto=".1f"
        )
        fig_refl.update_layout(xaxis_tickangle=-25, showlegend=False, height=450)
        st.plotly_chart(fig_refl, use_container_width=True)

# ==============================================================================
# MÓDULO 2: ANÁLISE INDIVIDUAL POR AUTOR
# ==============================================================================
elif menu == "🔍 Análise Individual por Autor":
    author_choice = st.selectbox(
        "Selecione um dos 7 autores:",
        df["name"].tolist()
    )
    
    author_row = df[df["name"] == author_choice].iloc[0]
    meta = AUTHORS_METADATA[author_row["key"]]
    text_sample = CORPUS_TEXTS[author_row["key"]]
    
    st.markdown(f"## {author_row['name']}")
    st.markdown(f"**Movimento Literário:** `{author_row['movement']}` | **Foco Analítico:** `{author_row['target']}`")
    
    st.markdown(f'<div class="quote-box">"{author_row["quote"]}"</div>', unsafe_allow_html=True)
    st.write(f"📌 **Hipótese de Pesquisa:** {author_row['hypothesis']}")
    
    st.markdown("---")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Riqueza Lexical (TTR)", f"{author_row['ttr']:.2%}")
    c2.metric("Palavras Únicas (Hapax)", f"{author_row['hapax']}")
    c3.metric("Média Palavras / Frase", f"{author_row['avg_words_sent']:.1f}")
    c4.metric("Frases Curtas (≤12 pal.)", f"{author_row['short_sent_pct']:.1f}%")
    
    st.markdown("### Trecho Literário Analisado:")
    st.text_area("", text_sample.strip(), height=160, disabled=True)
    
    st.markdown("### Palavras de Conteúdo Mais Frequentes:")
    top_words_df = pd.DataFrame(author_row["top_words"], columns=["Palavra", "Frequência"])
    fig_top = px.bar(
        top_words_df,
        x="Palavra",
        y="Frequência",
        color="Frequência",
        color_continuous_scale="Teal",
        text_auto=True
    )
    st.plotly_chart(fig_top, use_container_width=True)

# ==============================================================================
# MÓDULO 3: LABORATÓRIO DE NLP (TESTE SEU TEXTO)
# ==============================================================================
elif menu == "🧪 Laboratório de NLP (Teste seu Texto)":
    st.subheader("Laboratório Interativo de Estilometria")
    st.write("Digite ou cole uma redação, redação do ENEM ou texto literário para comparar suas métricas estilísticas com os clássicos:")
    
    user_input = st.text_area(
        "Insira seu texto aqui (mínimo 30 palavras para análise estatística):",
        height=180,
        placeholder="Cole aqui seu texto..."
    )
    
    if st.button("Analisar Estilo do Meu Texto", type="primary"):
        if len(user_input.strip().split()) < 15:
            st.warning("Por favor, insira um texto com pelo menos 15 palavras para podermos extrair métricas significativas.")
        else:
            profile = analyze_author_text(user_input, "user_text")
            lex = profile["lexical_diversity"]
            sent = profile["sentence_metrics"]
            refl = profile["reflection_vs_action"]
            
            st.success("Análise concluída com sucesso!")
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Suas Palavras", profile["tokens_count"])
            m2.metric("Riqueza Lexical (TTR)", f"{lex['ttr']:.2%}")
            m3.metric("Média Palavras / Frase", f"{sent['avg_words_per_sentence']:.1f}")
            m4.metric("Índice de Reflexão", f"{refl['reflection_ratio']:.1%}")
            
            # Stylistic comparison
            st.markdown("### Com quem seu estilo mais se parece?")
            if sent["avg_words_per_sentence"] < 10:
                st.info("🔹 **Seu estilo é conciso e direto!** Você usa frases curtas com impacto objetivo, aproximando-se da técnica de **Graciliano Ramos**.")
            elif sent["avg_words_per_sentence"] > 18:
                st.info("🔹 **Seu estilo é oratório e denso!** Você constrói períodos longos e elaborados, aproximando-se da cadência ensaística de **Euclides da Cunha**.")
            else:
                st.info("🔹 **Seu estilo tem cadência moderada e equilibrada**, próxima à narrativa de **Rachel de Queiroz** e **Jorge Amado**.")

# ==============================================================================
# MÓDULO 4: SOBRE O PROJETO & METODOLOGIA (ODS 4)
# ==============================================================================
elif menu == "📖 Sobre o Projeto & Metodologia (ODS 4)":
    st.subheader("Sobre o Projeto de Extensão Universitária")
    st.markdown("""
    **Nome do Projeto:** Dashboard Literário: Um Guia Tecnológico sobre os Clássicos da Literatura Brasileira  
    **Autor do Projeto:** **Luis Gustavo Rocha Lima** (1º Semestre)  
    **Instituição de Ensino:** **FMU — Centro Universitário das Faculdades Metropolitanas Unidas**  
    **Curso Vinculado:** Bacharelado em Ciência de Dados  
    **Área Temática:** Inovação, Tecnologia e Cultura Digital  
    **Linha de Extensão:** Educação e Letramento Digital  
    **Objetivo de Desenvolvimento Sustentável:** **ODS 4 – Educação de Qualidade (UNESCO/ONU)**  
    
    ---
    ### 🎯 Justificativa & Impacto Social
    Este projeto democratiza o acesso ao Processamento de Linguagem Natural (PLN), mostrando como a Ciência de Dados pode tornar o ensino de literatura mais visual, intuitivo e fascinante para estudantes do ensino médio e educadores.
    
    ### 🛠️ Tecnologias Utilizadas
    * **Linguagem:** Python
    * **Mineração & NLP:** NLTK, spaCy, Expressões Regulares, Dicionários Temáticos
    * **Visualização:** Matplotlib, Seaborn, Plotly Express, Streamlit
    * **Entrega:** Dashboard interativo em nuvem e Relatório Educativo em PDF
    """)
