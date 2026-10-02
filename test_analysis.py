"""
Test and benchmark script verifying stylistic & NLP metrics across the 7 authors.
"""

from src.corpus_data import CORPUS_TEXTS, AUTHORS_METADATA
from src.nlp_analyzer import analyze_author_text
import pandas as pd

def run_all_analyses():
    results = []
    print("=" * 70)
    print("DASHBOARD LITERÁRIO - RELATÓRIO PRELIMINAR DE NLP / ESTILOMETRIA")
    print("=" * 70)

    for author_key, text in CORPUS_TEXTS.items():
        meta = AUTHORS_METADATA[author_key]
        profile = analyze_author_text(text, author_key)
        
        lex = profile["lexical_diversity"]
        sent = profile["sentence_metrics"]
        thematic = profile["thematic_densities"]
        refl = profile["reflection_vs_action"]

        print(f"\n[{meta['name'].upper()}] - {meta['analysis_target']}")
        print(f"  • Total de Palavras: {profile['tokens_count']} | Sentenças: {profile['sentences_count']}")
        print(f"  • Riqueza Lexical (TTR): {lex['ttr']} | Hapax Legomena (termos únicos): {lex['hapax_legomena']} ({lex['hapax_ratio']*100:.1f}%)")
        print(f"  • Média Palavras/Frase: {sent['avg_words_per_sentence']} | % Frases Curtas: {sent['short_sentences_ratio']*100:.1f}%")
        print(f"  • Verbos: {refl['reflection_count']} Reflexão vs {refl['action_count']} Ação (Índice Introspectivo: {refl['reflection_ratio']*100:.1f}%)")
        
        # Highlight specific signature density
        if author_key == "rachel_de_queiroz":
            print(f"  • Densidade do Léxico de Seca/Escassez: {thematic['secura_escassez']['density_per_1k']:.2f} por 1.000 palavras")
        elif author_key == "jorge_amado":
            print(f"  • Densidade Cultural Baiana: {thematic['cultura_baiana']['density_per_1k']:.2f} por 1.000 palavras")
        elif author_key == "euclides_da_cunha":
            print(f"  • Densidade Termos Científico-Deterministas: {thematic['cientifico_determinista']['density_per_1k']:.2f} por 1.000 palavras")
        elif author_key == "ariano_suassuna":
            print(f"  • Densidade de Oralidade/Cordel/Interjeições: {thematic['oralidade_cordel']['density_per_1k']:.2f} por 1.000 palavras")

        results.append({
            "Autor": meta["name"],
            "Tokens": profile["tokens_count"],
            "TTR (Diversidade)": lex["ttr"],
            "Hapax Legomena": lex["hapax_legomena"],
            "Média Palavras/Frase": sent["avg_words_per_sentence"],
            "Frases Curtas (%)": round(sent["short_sentences_ratio"] * 100, 1),
            "Reflexão (%)": round(refl["reflection_ratio"] * 100, 1),
            "Seca/Escassez (Densidade)": thematic["secura_escassez"]["density_per_1k"],
            "Cultura Baiana (Densidade)": thematic["cultura_baiana"]["density_per_1k"],
            "Científico/Determinista": thematic["cientifico_determinista"]["density_per_1k"],
            "Oralidade/Cordel": thematic["oralidade_cordel"]["density_per_1k"],
        })

    df = pd.DataFrame(results)
    print("\n" + "=" * 70)
    print("TABELA COMPARATIVA RESUMIDA:")
    print("=" * 70)
    print(df.to_string(index=False))

    # Save summary dataframe to CSV
    df.to_csv("C:/Users/Luisg/.gemini/antigravity/scratch/dashboard_literario/data_summary.csv", index=False, encoding="utf-8-sig")
    print("\n[OK] Resumo salvo em 'data_summary.csv'")

if __name__ == "__main__":
    run_all_analyses()
