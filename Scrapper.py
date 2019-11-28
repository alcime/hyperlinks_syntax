""" Scrap les hyperliens d'une page html et les range dans un csv"""

import pandas as pd
from bs4 import BeautifulSoup


# Ask in prompt the name of the file
input_file_name = input("Name of the file :")
print ('\n')
if input_file_name == '':
   input_file_name = 'html_simple.html'

which_parser = "lxml"

   
#Open html and print it in terminal
with open(input_file_name, 'r') as html_file :
    html_txt = html_file.read()
    file_soup = BeautifulSoup(html_txt, features=which_parser)
    pretty_soup = file_soup.prettify()
    print (pretty_soup)

#

#i_where_link_starts = 0

while True: 
   i_where_link_starts = pretty_soup.find("a href")
   if i_where_link_starts == -1:
      print('Pas de liens')
   i_start_quote = pretty_soup.find('"', i_where_link_starts)
   i_end_quote = pretty_soup.find('"', i_start_quote + 1)
   url = pretty_soup[i_start_quote + 1: i_end_quote]
   pretty_soup = pretty_soup[i_end_quote:]
   if url:
      print(url)
   else :
      break


   
