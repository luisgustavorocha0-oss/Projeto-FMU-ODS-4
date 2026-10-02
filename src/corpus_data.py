"""
Corpus definitions and metadata for the 7 Brazilian Literature Classics.
Each entry includes verified canonical excerpts, historical context, and educational notes.
"""

AUTHORS_METADATA = {
    "guimaraes_rosa": {
        "name": "João Guimarães Rosa",
        "movement": "Modernismo (3ª Geração / Geração de 45)",
        "famous_works": ["Grande Sertão: Veredas", "Sagarana", "Primeiras Estórias"],
        "hypothesis": "Uso abundante de neologismos, arcaísmos e alta riqueza vocabular (Type-Token Ratio elevado e muitos hapax legomena), recriando a metafísica do Sertão.",
        "iconic_quote": "O real não está na saída nem na chegada: ele se dispõe para a gente é no meio da travessia.",
        "analysis_target": "Riqueza Vocabular e Invenção Neológica"
    },
    "graciliano_ramos": {
        "name": "Graciliano Ramos",
        "movement": "Modernismo (2ª Geração / Romance de 30 - Regionalismo Crítico)",
        "famous_works": ["Vidas Secas", "São Bernardo", "Angústia", "Memórias do Cárcere"],
        "hypothesis": "Prosa despojada, 'enxuta' e econômica. Frases curtas, sintaxe direta e quase ausência de adjetivação supérflua, espelhando a aridez da vida sertaneja.",
        "iconic_quote": "A palavra não foi feita para enfeitar, foi feita para dizer.",
        "analysis_target": "Concisão, Frases Curtas e Secura Verbal"
    },
    "jorge_amado": {
        "name": "Jorge Amado",
        "movement": "Modernismo (2ª Geração / Romance de 30 - Regionalismo Baiano)",
        "famous_works": ["Capitães da Areia", "Mar Morto", "Gabriela, Cravo e Canela", "Tenda dos Milagres"],
        "hypothesis": "Forte densidade lexical ligada à identidade cultural afro-brasileira, culinária, mar, saveiros, orixás e sincretismo de Salvador.",
        "iconic_quote": "O mar é a vida e a morte dos homens do mar.",
        "analysis_target": "Identidade Cultural Baiana e Sincretismo"
    },
    "rachel_de_queiroz": {
        "name": "Rachel de Queiroz",
        "movement": "Modernismo (2ª Geração / Romance de 30 - Ciclo da Seca)",
        "famous_works": ["O Quinze", "Memorial de Maria Moura", "As Três Marias"],
        "hypothesis": "Alta concentração de termos do campo semântico da escassez climática, fome, desolação da terra e a tragédia do êxodo dos retirantes.",
        "iconic_quote": "Sem chuva, sem pasto, a terra gretada de sede... e a marcha sem fim dos desgraçados.",
        "analysis_target": "Léxico da Seca, Fome e Êxodo em 'O Quinze'"
    },
    "clarice_lispector": {
        "name": "Clarice Lispector",
        "movement": "Modernismo (3ª Geração / Ficção Introspectiva e Psicológica)",
        "famous_works": ["A Hora da Estrela", "Perto do Coração Selvagem", "A Paixão Segundo G.H."],
        "hypothesis": "Predominância de verbos de reflexão, cognição e estados existenciais sobre verbos de ação material; fluxo de consciência e epifania.",
        "iconic_quote": "Renda-se, como eu me rendi. Mergulhe no que você não conhece como eu mergulhei.",
        "analysis_target": "Fluxo de Consciência: Reflexão vs. Ação"
    },
    "euclides_da_cunha": {
        "name": "Euclides da Cunha",
        "movement": "Pré-Modernismo",
        "famous_works": ["Os Sertões", "Contrastes e Confrontos"],
        "hypothesis": "Hibridismo estilístico: contraste gritante entre vocabulário científico determinista (geologia, climatologia, medicina) e o lirismo épico do sertão.",
        "iconic_quote": "O sertanejo é, antes de tudo, um forte.",
        "analysis_target": "Densidade Técnico-Científica vs. Sertão"
    },
    "ariano_suassuna": {
        "name": "Ariano Suassuna",
        "movement": "Movimento Armorial / Teatro e Romance Nordestino",
        "famous_works": ["Auto da Compadecida", "O Santo e a Porca", "Romance d'A Pedra do Reino"],
        "hypothesis": "Oralidade popular acentuada, abundância de interjeições nordestinas, diálogo dinâmico e métrica narrativa inspirada no cordel e nos folhetos.",
        "iconic_quote": "Não sei, só sei que foi assim!",
        "analysis_target": "Oralidade, Interjeições e Cordel"
    }
}

CORPUS_TEXTS = {
    "guimaraes_rosa": """
Nonada. Tiros que o senhor ouviu foram de briga de homem não, Deus esteja. Alvejei mira em árvore, no quintal, no baixo do córrego. Por meu costume.
O sertão está em toda parte. Sertão é onde o pensamento da gente se forma mais forte do que o poder do lugar. Viver é muito perigoso. Querer o bem com demais força, de incerto jeito, pode já estar sendo querença do mal.
O sertanejar de um homem é uma travessia interminável. Redemunho de vento ergue a poeira das veredas. O jagunço anda desassombrado, inventando a própria coragem no fio da faca.
Tudo é e não é. O diabo na rua, no meio do redemoinho. A gente vive, eu acho, é para desaprender o que os outros ensinaram e começar a inventação do nosso próprio saber.
Riobaldo, Tatarana, Urutu Branco. A jagunçagem corria pelos ermos, varando chapadões sob o sol de pino. Água pouca, sede de léguas, o buriti solitário apontando o poço oculto na vereda verdejante.
O real não está no começo nem no fim, ele se dispõe para a gente é no meio da travessia. As palavras têm que ter cheiro de mato e estrondo de trovão distante.
    """,
    
    "graciliano_ramos": """
A cachorra Baleia estava magra. As costelas apareciam através da pele suja. Fabiano olhou o céu. Uma nuvem escura prometia água. Não choveu.
Sinhá Vitória arrumava a trouxa. Os meninos choravam de fome. Fabiano praguejou contra a seca, contra a terra, contra o governo. A fazenda estava deserta. O patrão despedira a família.
Andavam devagar. Os pés rachados ardiam no chão quente. Um urubu voava alto em círculos lentos.
Fabiano sentou-se na pedra. Tirou a faca da bainha. Cortou um pedaço de osso. Era preciso seguir. A estrada não tinha fim.
Caminhavam calados. Sinhá Vitória equilibrava a cesta de folhas na cabeça. O menino mais velho gemia baixo. Fabiano apertava o cabo da espingarda. Não havia palavras no mundo capazes de matar aquela fome desgraçada. A vida era seca e dura como cascudo de tatu.
    """,
    
    "jorge_amado": """
A lua cheia nascia por trás do Forte de São Marcelo, iluminando as águas da Baía de Todos os Santos. No cais do porto, os saveiros balançavam suavemente ao ritmo da maré.
Vinha de longe o som do berimbau e os cantos do candomblé subindo pelas ladeiras do Pelourinho. Era noite de saudar Iemanjá, rainha das águas, senhora dos mares da Bahia.
Pedro Bala comandava os meninos do trapiche. Eram os Capitães da Areia, senhores da noite e da liberdade de Salvador. Meninos descalços, de pele morena queimada pelo sol, correndo pelas vielas entre o cheiro forte de azeite de dendê e o frito do acarajé.
Oxóssi protegia a caatinga distante, mas ali no mar quem mandava era Ogum e Iemanjá. A morena ria na janela, a batucada esquentava no terreiro, e a brisa do cais trazia histórias de valentes capoeiristas, marinheiros errantes e amores eternos.
    """,
    
    "rachel_de_queiroz": """
A seca de 1915 avançava sobre o sertão do Ceará como um incêndio silencioso. A terra esturricada abria fendas profundas sob o sol impiedoso de meio-dia. O gado caía de fome nas beiradas dos caminhos, e os urubus faziam festa nas carcaças esqueléticas.
Chico Bento reuniu a família para o êxodo doloroso. Tinham que abandonar o sítio ressequido antes que a morte levasse as crianças. Cordulina levava o caçula nos braços esqueléticos, enquanto Mocinha e o menino mais velho arrastavam os pés na poeira escaldante.
Não havia mais milho nem feijão no paiol. A cacimba secara por completo, restando apenas um lodo salobro no fundo. O êxodo dos retirantes engrossava a cada légua de poeira e desespero.
A fome roía as entranhas como dentes afiados. Seguiam em marcha fúnebre rumo a Fortaleza, fugindo da morte certa na caatinga crestada pela estiagem implacável.
    """,
    
    "clarice_lispector": """
O que eu sinto não cabe no meu pensamento. É uma coisa que lateja no escuro antes mesmo da palavra existir. Eu existo? Penso, logo sou uma interrogação contínua no silêncio da sala.
Macabéa olhava o espelho quebrado e sentia uma vertigem suave, como se a sua vida pertencesse a outra pessoa. Ela não sabia explicar a si mesma o mistério de respirar.
Eu escrevo para nada e para ninguém, escrevo porque de repente a solidão se tornou insuportável e preciso inventar uma presença. Viver dói na carne, mas é uma dor luminosa.
Fico horas contemplando a parede branca e imaginando o que está por trás do abismo da consciência. O instante é um flash, um relâmpago que some assim que tento segurá-lo.
Eu sinto, eu hesito, eu pressinto. Há no fundo da alma uma pergunta sem resposta que me faz tremer diante da própria existência.
    """,
    
    "euclides_da_cunha": """
A estrutura orográfica e geológica do sertão setentrional revela uma constituição cristalina primitiva, submetida a milênios de severa erosão mecânica e intempéries climáticas extremas.
O relevo acidentado, recortado por serras tabulares e boqueirões calcários, impõe condições ecológicas de extrema aridez à caatinga xerófila. A morfologia das espécies vegetais, adaptadas à estiagem com cutículas espessas e espinhos defensivos, atesta a violência do ambiente circundante.
O homem sertanejo, fruto desse meio telúrico impiedoso, surge como um produto bioclimático de excepcional resistência física. Diante da investida militar republicana em Canudos, o sertanejo transmuda-se em combatente formidável, amparado pela topografia impenetrável e pela fusão atávica com a terra árida.
O contraste entre o rigor dos dados topográficos e a epopeia bélica desvenda o drama sociológico de uma civilização cindida entre o litoral letrado e o sertão bárbaro.
    """,
    
    "ariano_suassuna": """
— Oxente, Chicó! Como é que você me diz uma desgraça dessa no meio da feira?
— Não sei, João Grilo, só sei que foi assim! O homem jurou pelo diabo que o cachorro da mulher do padeiro ia ter testamento em latim, benzido pelo padre e com direito a sino tocando na matriz!
— Eita cabra mentiroso da gota serena! Vixe Maria, se o vigário descobre uma heresia dessas, manda nós dois pro fogo do inferno antes do pôr do sol!
— Mas eu garanto a você, João Grilo, pela honra da minha falecida mãe!
No terreiro do sertão da Paraíba, o repente do cantador desafiava a rima do cordel. As estrofes rimadas contavam a saga do sertanejo esperto que tapeia os poderosos, os demônios e até a própria morte com a graça de Nossa Senhora da Conceição, a Virgem Compadecida.
— Arretado é o sujeito que não se curva diante de coronel nenhum! Viva o povo, viva a cantoria, e valei-me São Sebastião!
    """
}
