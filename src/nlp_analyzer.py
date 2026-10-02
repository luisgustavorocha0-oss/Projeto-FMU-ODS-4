"""
Core NLP and Stylometry Engine for 'Dashboard Literário'.
Analyzes Brazilian literary classics across 7 stylistic and thematic dimensions.
"""

import re
import math
from collections import Counter
from typing import Dict, List, Any, Tuple

# Portuguese stopwords list for pure-Python fallback (without relying exclusively on external downloads)
STOPWORDS_PT = {
    'de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'é', 'com', 'não', 'uma',
    'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele',
    'das', 'tem', 'à', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'há', 'nos', 'já',
    'está', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'era',
    'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 'nas', 'me', 'esse', 'eles',
    'estão', 'você', 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha',
    'têm', 'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'será', 'nós', 'tenho', 'lhe',
    'deles', 'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te', 'vocês', 'vos',
    'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas',
    'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto',
    'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve', 'estivemos', 'estiveram',
    'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 'estejam',
    'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'há',
    'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos',
    'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei',
    'houverá', 'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos',
    'são', 'era', 'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja',
    'sejamos', 'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'será',
    'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'tenho', 'tem', 'temos', 'tém', 'tinha',
    'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tivéramos', 'tenha',
    'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver', 'tivermos', 'tiverem',
    'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam', 'sob', 'sobre', 'onde'
}

# Thematic lexicons for specific research questions in the proposal
LEXICONS = {
    "secura_escassez": {
        "seca", "sol", "calor", "fome", "poeira", "morte", "retirantes", "sede", "sertão",
        "terra", "cinza", "esturricada", "esqueleto", "garganta", "brasa", "queimada",
        "estiagem", "aridez", "gretada", "urubus", "miséria", "catinga", "caatinga", "exôdo", "desgraça"
    },
    "cultura_baiana": {
        "bahia", "salvador", "mar", "cais", "porto", "saveiro", "dende", "dendê", "acaraje", "acarajé",
        "orixá", "iemanjá", "ogum", "oxóssi", "candomble", "candomblé", "santo", "festa", "tabuleiro",
        "capoeira", "berimbau", "malandro", "morena", "mulata", "batucada", "axé", "pelourinho", "ladeira"
    },
    "cientifico_determinista": {
        "estrato", "geologia", "climático", "relevo", "topografia", "zona", "bacia", "planalto",
        "erosão", "temperatura", "pressão", "fenômeno", "hipótese", "raça", "atavismo", "degenerescência",
        "morfologia", "fisiologia", "psicologia", "ambiente", "condição", "evolução", "biológico"
    },
    "oralidade_cordel": {
        "oxente", "vixe", "eita", "uai", "arretado", "diabo", "padre", "cabra", "valei-me", "nossa",
        "senhora", "sinhô", "sinhó", "compadre", "comadre", "bichinho", "danado", "cuscuz", "sertanejo",
        "verso", "rima", "peleja", "desafio", "martelo", "repente", "glosa"
    },
    "verbos_reflexao_existenciais": {
        "pensar", "sentir", "ser", "estar", "parecer", "existir", "lembrar", "saber", "compreender",
        "imaginar", "duvidar", "viver", "perceber", "sonhar", "olhar", "meditar", "refletir", "angustiar",
        "morrer", "calcular", "achar", "pressentir", "doer", "amar", "esquecer", "intuir", "hesitar"
    },
    "verbos_acao": {
        "correr", "andar", "bater", "gritar", "pular", "pegar", "puxar", "atirar", "matar", "fugir",
        "carregar", "cortar", "caminhar", "abrir", "fechar", "subir", "descer", "marchar", "lutar",
        "construir", "atacar", "partir", "seguir", "empurrar", "romper", "viajar", "entrar", "sair"
    }
}


def tokenize_words(text: str) -> List[str]:
    """Tokenize text into lowercase alphabetic words."""
    return re.findall(r'\b[a-záàâãéèêíïóôõöúçñ]+\b', text.lower())


def tokenize_sentences(text: str) -> List[str]:
    """Split text into sentences handling typical abbreviations."""
    # Simple, robust sentence splitter for literary Portuguese
    sentences = re.split(r'(?<=[.!?…])\s+(?=[A-ZÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇ0-9"\'“«])', text.strip())
    return [s.strip() for s in sentences if len(s.strip()) > 3]


def compute_lexical_diversity(tokens: List[str]) -> Dict[str, Any]:
    """
    Computes Type-Token Ratio (TTR), Hapax Legomena count, and vocabulary richness.
    Crucial for Guimarães Rosa (neologisms, vast vocabulary).
    """
    if not tokens:
        return {"ttr": 0.0, "total_tokens": 0, "unique_tokens": 0, "hapax_legomena": 0, "hapax_ratio": 0.0}

    counts = Counter(tokens)
    total_tokens = len(tokens)
    unique_tokens = len(counts)
    hapax = sum(1 for w, c in counts.items() if c == 1)

    return {
        "ttr": round(unique_tokens / total_tokens, 4),
        "total_tokens": total_tokens,
        "unique_tokens": unique_tokens,
        "hapax_legomena": hapax,
        "hapax_ratio": round(hapax / unique_tokens, 4) if unique_tokens else 0.0
    }


def compute_sentence_metrics(sentences: List[str]) -> Dict[str, Any]:
    """
    Computes sentence length statistics and conciseness.
    Crucial for Graciliano Ramos (short, dry, dense sentences).
    """
    if not sentences:
        return {"avg_words_per_sentence": 0.0, "median_words": 0, "short_sentences_ratio": 0.0, "total_sentences": 0}

    word_counts = [len(tokenize_words(s)) for s in sentences if len(tokenize_words(s)) > 0]
    if not word_counts:
        return {"avg_words_per_sentence": 0.0, "median_words": 0, "short_sentences_ratio": 0.0, "total_sentences": 0}

    avg_words = sum(word_counts) / len(word_counts)
    short_sentences = sum(1 for c in word_counts if c <= 12)  # sentences with <= 12 words

    return {
        "avg_words_per_sentence": round(avg_words, 2),
        "min_words": min(word_counts),
        "max_words": max(word_counts),
        "short_sentences_ratio": round(short_sentences / len(word_counts), 4),
        "total_sentences": len(sentences),
        "sentence_lengths": word_counts
    }


def compute_lexicon_density(tokens: List[str], lexicon_name: str) -> Dict[str, Any]:
    """
    Calculates presence and density (per 1,000 words) of a thematic lexicon.
    """
    target_words = LEXICONS.get(lexicon_name, set())
    if not tokens or not target_words:
        return {"density_per_1k": 0.0, "matches_count": 0, "top_words": []}

    matches = [w for w in tokens if w in target_words]
    density = (len(matches) / len(tokens)) * 1000.0

    return {
        "density_per_1k": round(density, 2),
        "matches_count": len(matches),
        "top_words": Counter(matches).most_common(10)
    }


def compute_reflection_vs_action(tokens: List[str]) -> Dict[str, Any]:
    """
    Compares reflection/existential verbs vs action verbs.
    Crucial for Clarice Lispector (stream of consciousness vs action).
    """
    refl_set = LEXICONS["verbos_reflexao_existenciais"]
    act_set = LEXICONS["verbos_acao"]

    refl_matches = [w for w in tokens if w in refl_set]
    act_matches = [w for w in tokens if w in act_set]

    total_verbs = len(refl_matches) + len(act_matches)
    ratio = round(len(refl_matches) / total_verbs, 4) if total_verbs > 0 else 0.5

    return {
        "reflection_count": len(refl_matches),
        "action_count": len(act_matches),
        "reflection_ratio": ratio,
        "reflection_top": Counter(refl_matches).most_common(5),
        "action_top": Counter(act_matches).most_common(5)
    }


def get_top_content_words(tokens: List[str], top_n: int = 15) -> List[Tuple[str, int]]:
    """Get the most frequent non-stopword tokens."""
    content_tokens = [w for w in tokens if w not in STOPWORDS_PT and len(w) > 2]
    return Counter(content_tokens).most_common(top_n)


def analyze_author_text(text: str, author_key: str) -> Dict[str, Any]:
    """
    Runs complete stylistic and thematic profiling for a given literary text.
    """
    tokens = tokenize_words(text)
    sentences = tokenize_sentences(text)

    lex_div = compute_lexical_diversity(tokens)
    sent_metrics = compute_sentence_metrics(sentences)
    top_words = get_top_content_words(tokens)
    refl_vs_act = compute_reflection_vs_action(tokens)

    # Specific thematic scans
    sec_density = compute_lexicon_density(tokens, "secura_escassez")
    cba_density = compute_lexicon_density(tokens, "cultura_baiana")
    det_density = compute_lexicon_density(tokens, "cientifico_determinista")
    cordel_density = compute_lexicon_density(tokens, "oralidade_cordel")

    return {
        "author_key": author_key,
        "tokens_count": len(tokens),
        "sentences_count": len(sentences),
        "lexical_diversity": lex_div,
        "sentence_metrics": sent_metrics,
        "top_content_words": top_words,
        "reflection_vs_action": refl_vs_act,
        "thematic_densities": {
            "secura_escassez": sec_density,
            "cultura_baiana": cba_density,
            "cientifico_determinista": det_density,
            "oralidade_cordel": cordel_density
        }
    }
