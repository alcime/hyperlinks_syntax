""" Scrape les hyperliens d'une page html du New York Times et les range dans un csv"""


# Libraries
import pandas as pd
from bs4 import BeautifulSoup
import re
import argparse

# Create a parser for the terminal
t_parser = argparse.ArgumentParser(description = 'Parse an html file for hyperlinks and returns a tsv file.', epilog='Hope it helped !')

# Create arguments the parser will look for
t_parser.add_argument('--verbose', '-v', dest = 'print_in_console', action='store_true', help = 'Print the intermediate step in the console (default is false)')
t_parser.add_argument('input_file_name', metavar='relative_path_name', action='store', help= 'Enter the relative pathname of the file you want to scrap')
t_parser.add_argument('-out' ,metavar='output_file_name', action='store', default='scrapped_url.tsv',help= 'Name of the tsv file where the scraped hyperlinks will be stored (default is \'scrapped.url\')')
t_parser.add_argument('-which_parser', metavar='Name of the parser', action='store', default='lxml',help= 'Name of the parser (default is \'lxml\')')
t_parser.add_argument('-tag_class_hyperlinks', metavar='Class tag for hyperlinks used by site', action='store', default='a class="css-1g7m0tk" href', help='Class of the tag of the hyperlink')

parsed = t_parser.parse_args()

# Variables
input_file_name = parsed.input_file_name
print_in_console = parsed.print_in_console
output_file_relative_pathname = parsed.out
which_parser = parsed.which_parser
tag_class_hyperlinks = parsed.tag_class_hyperlinks


# Functions
def format_string (string):
   """ Delete newlines, tabulations and leading space in a string"""
   string_formatted = string.replace('\n', '')
   string_formatted = string_formatted.replace('\t', '')
   string_formatted = re.sub(r"^\s+", "", string_formatted) # Remove leading spaces
   return string_formatted

def delete_irrelevant_tags_proper_to_nyt (soup):
   """ Format the whole page to delete some tags that could get in the way of the parser."""
   soup_formatted = soup.replace('title=""','')
   # The em tag is used for nyt adds
   soup_formatted = soup_formatted.replace ('<em class="css-2fg4z9 e1gzwzxm0">' , '')
   soup_formatted = soup_formatted.replace ('</em>', '')
   # Delete paragraphs tags proper to nyt
   soup_formatted = soup_formatted.replace ('</p><div id="NYT_MID_MAIN_CONTENT_REGION" class="css-9tf9ac"></div><p class="css-exrw3m evys1bk0">', '')
   return soup_formatted

# Open a tsv to write the data in it
output_file = open(output_file_relative_pathname, "w+")
output_file.write('url' + '\t' + 'hyperlinked text' + '\n')

# Open html and print it in prompt
with open(input_file_name, 'r') as html_file :
    html_file_contents = html_file.read()
    file_soup = BeautifulSoup(html_file_contents, features=which_parser)
    pretty_soup = file_soup.prettify()
    pretty_soup = delete_irrelevant_tags_proper_to_nyt(pretty_soup)
    if print_in_console:
       print ('Here is your web page formatted:\n' + pretty_soup + '\n')


# Loop over the html page to find hyperlinked text and associated url

if print_in_console == True:
   print ('I found the following links :')

while True: 
   # Extract the url
   i_where_link_starts = pretty_soup.find(tag_class_hyperlinks)
   
   if i_where_link_starts == -1:
      print('\nFound everything, end of process')
      break

   i_start_quote = pretty_soup.find('"', i_where_link_starts + len(tag_class_hyperlinks) )
   i_end_quote = pretty_soup.find('"', i_start_quote + 1)
   url = pretty_soup[i_start_quote + 1: i_end_quote]

   # Extract the hyperlinked text   
   i_start_hyperlinked = pretty_soup.find('>', i_end_quote)
   i_end_hyperlinked = pretty_soup.find('</a>', i_start_hyperlinked + 1)
   hyperlinked = pretty_soup[i_start_hyperlinked + 1 : i_end_hyperlinked]

   # Extract the text before and after the hyperlinked part
   i_start_sentence = re.search("\.\s+\"*[A-Z][a-z]+", pretty_soup[i_start_hyperlinked - 200:]).start()
   #print(re.search("\.\s+\"*[A-Z][a-z]+", pretty_soup[i_start_hyperlinked - 200:]))
   
   i_start_sentence_full = i_start_sentence + len(pretty_soup[:i_start_hyperlinked - 200])

   #print(i_start_sentence)
   #print(len(pretty_soup[:i_start_hyperlinked - 200]))
   print(i_start_sentence_full)
   print(i_start_hyperlinked)
   
   i_end_sentence = re.search("\.", pretty_soup[i_end_hyperlinked:]).start()
   i_end_sentence_full = i_end_sentence + len(pretty_soup[:i_end_hyperlinked])
   print(i_end_hyperlinked)
   print(i_end_sentence_full)
   
   sentence = pretty_soup[i_start_sentence_full: i_start_hyperlinked] + pretty_soup[i_end_hyperlinked: i_end_sentence_full]
   #print(sentence)
   
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
