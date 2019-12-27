# hyperlinks_syntax
Projet d'analyse quantitative de la syntaxe des hyperliens. Le but est de recuperer les hyperliens ainsi que leur destination pour analyser ensuite leur categorie grammaticale afin de voir si la majorite des hyperliens sont des syntagmes usuels (en syntaxe).

Ce projet se compose de deux programmes: un scraper et un analyzer.

# Louis-Marie:

Je me suis chargé de la partie scraper.

Le scraper, a partir d'une page HTML du New York Times, recupere dans les colonnes d'un fichier TSV les donnees suivantes:
1. partie du texte qui est hyperlinkée 
2. destination de l'hyperlien.


Contexte : 

Je n'avais jamais programme avant, même si j'avais appris à utiliser le terminal, et j'ai commencé Python cette année, en utilisant Emacs comme environnement.

J'ai essayé d'integrer autant de notions que possibles (définition de fonction, Regex, ... ) dans mon programme, et surtout de le construire sans utiliser un parser (la library BeautifulSoup n'est utilisée que pour du formatage). Ceci a engendré plusieurs limitations : tout d'abord, le scraper est construit spécialement pour des pages du New York Times (même si la variable tag_class peut-être changée en fonction des balises utilisées par le site). De plus, il m'a fallu reconstruire certaines fonctions d'un parseur à la main, par exemple pour le formatage du texte que l'on scrape.


# Anastasia:

Moi je me suis chargée de la partie analyzer.

L'analyzer, a partir du fichier TSV que le scraper a produit associe le text hyperlinké à sa catégorie syntaxique. Ensuite, il produit un graph qui montre la distribution des catégories syntaxiques dans le texte hyperlinké. 

Ceci est fait à l'aide de la librairie NLTK. Par conséquent, les catégories syntaxiques utilisées sont celles de NLTK et le programme marche pour un texte en anglais. Le fichier TSV est d'abord transformé en Panda DataFrame et ensuite le programme associe à l'aide du NLTK POS Tagger le mot hyperlinké avec sa catégorie syntaxique. 

Dans un deuxième temps, le programme produit un graph à l'aide de la librairie matplotlib. Ainsi, il montre dans un diagramme circulaire le pourcentage de chaque catégorie utilisée.

Contexte: 

J'étais complétement débutante n'ayant jamais programmé avant, ne connaissant même pas la fonction du terminal. J'ai commencé donc Python avec ce cours, j'ai appris comment utilisé le terminal et j'ai programmé cet analyzer utilisant Spyder dans Anaconda Navigator. 

J'ai fait de mon mieux pour que le programme soit lisible et simple, utilisant uni NLTK, pandas et matplotlib. J'ai utilisé plusiers fois Stack Overflow quand j'avais des questions, surtout pour la syntaxe de Python et pour comprendre ce que font certaines fonctions de NLTK et de pandas. En plus, j'ai discuté avec Louis-Marie quand j'avais des doutes et/ou des problèmes quand à la conception de l'algorithme. J'ai trouvé cet échange très utile et j'ai beaucoup aimé faire ce projet en groupe. 

