""" Scrape les hyperliens d'une page html du New York Times et les range dans un csv"""


# Libraries
import pandas as pd
from bs4 import BeautifulSoup
import re
from argparse import ArgumentParser

# Variables
tag_class_hyperlinks = 'a class="css-1g7m0tk" href'
which_parser = "lxml"
print_in_console = True
output_file_relative_pathname = 'scrapped_url.tsv'

# Create a parser for the terminal
#t_parser = ArgumentParser()

#t_parser.add_argument("-f", "--file", dest="filename", help="Relative path of the html file you want to scrape ", default = 'html_simple.html')
#t_parser.add_argument("-v+", "--verbose", action="store_true", dest="verbose", default=True, help="Print the results of intermediate steps in terminal")
#t_parser.add_argument("-p", "--parser", dest="parser_type", default="lxml", help="Type of the parser")

#args = t_parser.parse_args()

#input_file_name = args.filename
#which_parser = args.parser_type
#xprint_in_console = args.verbose


# Functions
def format_string (string):
   """ Delete newlines, tabulations and leading space in a string"""
   string_formatted = string.replace('\n', '')
   string_formatted = string_formatted.replace('\t', '')
   string_formatted = re.sub(r"^\s+", "", string_formatted) # Remove leading spaces
   return string_formatted


# Ask in prompt the name of the file
input_file_name = input("Name of the file :")
print ('\n')
if input_file_name == '':
   input_file_name = 'html_simple.html'


# Open a tsv to write the data in it
output_file = open(output_file_relative_pathname, "w+")
output_file.write('url' + '\t' + 'hyperlinked text' + '\n')

# Open html and print it in prompt
with open(input_file_name, 'r') as html_file :
    html_file_contents = html_file.read()
    file_soup = BeautifulSoup(html_file_contents, features=which_parser)
    pretty_soup = file_soup.prettify()
    pretty_soup = pretty_soup.replace('title=""','')
    if print_in_console:
       print (pretty_soup)


# Loop over the html page to find hyperlinked text and associated url

while True: 
   # Extract the url
   i_where_link_starts = pretty_soup.find(tag_class_hyperlinks)
   
   if i_where_link_starts == -1:
      print('No more links')
      break

   i_start_quote = pretty_soup.find('"', i_where_link_starts + len(tag_class_hyperlinks) )
   i_end_quote = pretty_soup.find('"', i_start_quote + 1)
   url = pretty_soup[i_start_quote + 1: i_end_quote]

   if url == None :
      print('No more links')
      break

   
   # Extract the hyperlinked text   
   i_start_hyperlinked = pretty_soup.find('>', i_end_quote)
   i_end_hyperlinked = pretty_soup.find('</a>', i_start_hyperlinked + 1)
   hyperlinked = pretty_soup[i_start_hyperlinked + 1 : i_end_hyperlinked]

   # Format the url and the hyperlinked text
   url_formatted = format_string(url)
   hyperlinked_formatted = format_string(hyperlinked)
   
   # Delete the part the Scraper already processed
   pretty_soup = pretty_soup[i_end_quote:]

   

   # Delete false positives by checking approximately if the url is not part of a script (this is because when embedded in javascript code, double slash will be coded as '/\/\' in the html code source)
   if url.find('\/\/') == -1 :
      
      # Write the data in tsv
      if print_in_console :
         #print(":".join("{:02x}".format(ord(char)) for char in hyperlinked_formatted)) Debugging lines to check the hexadecimal of the data
         #print(":".join("{:02x}".format(ord(char)) for char in url_formatted))
         print(url_formatted + '\t' +  hyperlinked_formatted)
         #print (":".join("{:02x}".format(ord(char)) for char in url_formatted + hyperlinked_formatted))
      output_file.write(url_formatted + '\t' + hyperlinked_formatted + '\n')
   
   

output_file.close()
