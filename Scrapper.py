""" Scrap les hyperliens d'une page html et les range dans un csv"""

import pandas as pd
from bs4 import BeautifulSoup


# Demande le nom du fichier
input_file_name = input("Nom du fichier d'entree :")
print ('\n')
if input_file_name == '':
   input_file_name = 'html_simple.html'

which_parser = "lxml"

   
#
with open(input_file_name, 'r') as html_file :
    html_txt = html_file.read()
    file_soup = BeautifulSoup(html_txt, features=which_parser)
    pretty_soup = file_soup.prettify()
    print (pretty_soup)

#



while True :
    find_where_link_starts = pretty_soup.find("a href")
    print (find_where_link_starts)
    if find_where_link_starts == -1:
        print('Pas de liens')
    start_quote = file_soup.find('"', find_where_link_starts)
    #print (type(start_quote))
    end_quote = file_soup.find('"', start_quote + 1)
    url = file_soup[start_quote + 1: end_quote]
    file_soup = file_soup[end_quote:]
    if url:
        print(url)
    else:
        break

   
