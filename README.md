# hyperlinks_syntax
Projet d'analyse quantitative de la syntaxe des hyperliens. Le but est de recuperer les hyperliens ainsi que leur destination pour analyser ensuite leur categorie grammaticale afin de voir si la majorite des hyperliens sont des syntagmes usuels en syntaxe.

Ce projet se compose de deux programmes: un scraper et un analyzer.

Je me suis charge de la partie scraper. (Louis-Marie)

Le scraper, a partir d'une page HTML du Washington Post, recupere dans les colonnes d'un fichier TSV les donnees suivantes:
1. partie du texte qui est hyperlinkee 
2. destination de l'hyperlien.


Contexte : Je n'avais jamais programme avant, meme si j'avais appris a utiliser le terminal, et j'ai commence Python cette annee.
J'ai essaye d'integrer autant de notions que possibles (definition de fonction, Regex, ... ) dans mon programme, et surtout de le construire sans utiliser un parser (la library BeautifulSoup n'est utilisee que pour du formatage). Ceci a engendre plusieurs limitations : tout d'abord, le scraper est construit specialement pour des pages du Washington Post. De plus, il m'a fallu reconstruire certaines fonctions d'un parseur a la main, par exemple le formatage du texte que l'on scrape.



L'analyzer, a partir d'un fichier csv [A completer]
