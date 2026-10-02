"""
Generates publication-quality charts for the Educational Report (Matplotlib / Seaborn).
Produces visual figures directly aligned with the project scope:
- Sentence length comparison (Graciliano vs. Euclides vs. others)
- Thematic signature heatmap (Bahia, Seca, Ciência, Cordel)
- Verb classification (Reflection vs. Action - Clarice Lispector)
- Lexical Diversity & Hapax Legomena (Guimarães Rosa)
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def generate_all_figures(output_dir: str = "reports/figures"):
    os.makedirs(output_dir, exist_ok=True)
    
    # Load summary data
    df = pd.read_csv("data_summary.csv")
    
    # Set overall aesthetic style
    sns.set_theme(style="whitegrid", palette="deep")
    plt.rcParams.update({'font.sans-serif': 'DejaVu Sans', 'font.size': 11})

    # =========================================================================
    # Figure 1: Concisão Sintática - Média de Palavras por Frase e % Frases Curtas
    # (Foco: Graciliano Ramos vs. Euclides da Cunha)
    # =========================================================================
    fig, ax1 = plt.subplots(figsize=(10, 5.5))
    
    colors = ['#2b5c8f' if a != 'Graciliano Ramos' and a != 'Euclides da Cunha' 
              else ('#d95f02' if a == 'Graciliano Ramos' else '#7570b3') 
              for a in df['Autor']]
    
    bars = ax1.bar(df['Autor'], df['Média Palavras/Frase'], color=colors, width=0.55, edgecolor='black', alpha=0.85)
    ax1.set_ylabel("Média de Palavras por Frase", fontsize=12, fontweight='bold', color='#1a1a1a')
    ax1.set_title("Estilometria Sintática: Extensão Média de Frases nos Clássicos Brasileiros\n(Destaque para a secura de Graciliano Ramos vs. a oratória de Euclides da Cunha)", fontsize=13, pad=15)
    plt.xticks(rotation=25, ha='right', fontsize=10)
    
    # Add data values above bars
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f"{yval:.1f} pal.", ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax1.set_ylim(0, max(df['Média Palavras/Frase']) + 4)
    plt.tight_layout()
    fig1_path = os.path.join(output_dir, "fig1_extensao_sentencas.png")
    plt.savefig(fig1_path, dpi=300)
    plt.close()
    print(f"[OK] Gerada: {fig1_path}")

    # =========================================================================
    # Figure 2: Matriz de Calor de Densidade Temática (Assinaturas Lexicais)
    # (Jorge Amado, Rachel de Queiroz, Euclides da Cunha, Ariano Suassuna)
    # =========================================================================
    fig, ax = plt.subplots(figsize=(9, 6))
    thematic_cols = ['Seca/Escassez (Densidade)', 'Cultura Baiana (Densidade)', 'Científico/Determinista', 'Oralidade/Cordel']
    heatmap_data = df.set_index('Autor')[thematic_cols]
    
    sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlOrRd", cbar_kws={'label': 'Densidade (ocorrências / 1.000 palavras)'}, linewidths=1, ax=ax)
    ax.set_title("Assinaturas Temáticas e Léxicas por Autor (NLP)\n(Comprovando as hipóteses temáticas de cada obra)", fontsize=13, pad=15)
    ax.set_ylabel("")
    ax.set_xlabel("Campo Semântico / Léxico Analisado", fontweight='bold', fontsize=11)
    plt.xticks(rotation=20, ha='right')
    plt.tight_layout()
    fig2_path = os.path.join(output_dir, "fig2_heatmap_tematico.png")
    plt.savefig(fig2_path, dpi=300)
    plt.close()
    print(f"[OK] Gerada: {fig2_path}")

    # =========================================================================
    # Figure 3: Clarice Lispector - Proporção de Verbos (Reflexão vs Ação)
    # =========================================================================
    fig, ax = plt.subplots(figsize=(8, 5))
    refl_df = df.sort_values(by="Reflexão (%)", ascending=False)
    colors_refl = ['#e7298a' if a == 'Clarice Lispector' else '#66a61e' for a in refl_df['Autor']]
    
    bars = ax.barh(refl_df['Autor'], refl_df['Reflexão (%)'], color=colors_refl, edgecolor='black', alpha=0.85)
    ax.set_xlabel("Índice de Verbos Introspectivos / Existenciais (%)", fontweight='bold', fontsize=11)
    ax.set_title("Mapeamento do Fluxo de Consciência: Predomínio de Verbos Existenciais\n(Clarice Lispector com 100% de verbos de cognição/sentir no excerto)", fontsize=12, pad=15)
    ax.set_xlim(0, 110)
    
    for bar in bars:
        w = bar.get_width()
        ax.text(w + 2, bar.get_y() + bar.get_height()/2.0, f"{w:.1f}%", ha='left', va='center', fontweight='bold', fontsize=10)

    plt.tight_layout()
    fig3_path = os.path.join(output_dir, "fig3_clarice_reflexao.png")
    plt.savefig(fig3_path, dpi=300)
    plt.close()
    print(f"[OK] Gerada: {fig3_path}")

    # =========================================================================
    # Figure 4: Riqueza Lexical (TTR) e Hapax Legomena (Guimarães Rosa)
    # =========================================================================
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(len(df['Autor']))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, df['TTR (Diversidade)'] * 100, width, label='Riqueza Lexical (TTR %)', color='#1b9e77', edgecolor='black')
    bars2 = ax.bar(x + width/2, (df['Hapax Legomena'] / df['Tokens']) * 100, width, label='Palavras Únicas / Hapax (%)', color='#d95f02', edgecolor='black')
    
    ax.set_ylabel("Percentual (%)", fontweight='bold')
    ax.set_title("Diversidade Vocabular e Invenção Lexical (TTR e Hapax Legomena)", fontsize=13, pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(df['Autor'], rotation=25, ha='right')
    ax.legend(loc='lower right', frameon=True)
    ax.set_ylim(0, 100)
    
    plt.tight_layout()
    fig4_path = os.path.join(output_dir, "fig4_riqueza_vocabular.png")
    plt.savefig(fig4_path, dpi=300)
    plt.close()
    print(f"[OK] Gerada: {fig4_path}")

if __name__ == "__main__":
    generate_all_figures()
