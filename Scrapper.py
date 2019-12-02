""" Scrape les hyperliens d'une page html et les range dans un csv"""

import pandas as pd
from bs4 import BeautifulSoup


# Ask in prompt the name of the file
input_file_name = input("Name of the file :")
print ('\n')
if input_file_name == '':
   input_file_name = 'html_simple.html'

which_parser = "lxml"
print_in_console = True
output_file_relative_pathname = 'scrapped_url.tsv'


# Open a tsv to write the data in it
output_file = open(output_file_relative_pathname, "w+")

   
# Open html and print it in terminal
with open(input_file_name, 'r') as html_file :
    html_file_contents = html_file.read()
    file_soup = BeautifulSoup(html_file_contents, features=which_parser)
    pretty_soup = file_soup.prettify()
    if print_in_console:
       print (pretty_soup)

#

# Loop over the html page to find hyperlinked text and associated url

while True: 
   # Extract the url
   i_where_link_starts = pretty_soup.find("href=")

   if i_where_link_starts == -1:
      print('Pas de liens')
      break

   i_start_quote = pretty_soup.find('"', i_where_link_starts)
   i_end_quote = pretty_soup.find('"', i_start_quote + 1)
   url = pretty_soup[i_start_quote + 1: i_end_quote]

   if url == None :
      print('No more links')
      break

   
   # Extract the hyperlinked text   
   i_start_hyperlinked = pretty_soup.find('>', i_end_quote)
   i_end_hyperlinked = pretty_soup.find('</a>', i_start_hyperlinked + 1)
   hyperlinked = pretty_soup[i_start_hyperlinked + 1 : i_end_hyperlinked]

   # Delete the part the Scraper already processed
   pretty_soup = pretty_soup[i_end_quote:]

   

   # Check if the url is not part of a script
   if url.find('\/\/') == -1 :
      # Write the data in tsv
      if print_in_console :
         print(":".join("{:02x}".format(ord(char)) for char in hyperlinked))
         print(url + hyperlinked)
      output_file.write(url + '\t' + hyperlinked)
   
   

output_file.close()
