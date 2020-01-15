""" From a csv file, we calculate the proportion of certain syntactic structures found in the hyperlink """


import pandas as pd
import nltk # we use the library NLTK to associate the hyperlink text with certain syntactic categories
import matplotlib.pyplot as plt
import re


# download required packages from NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')


input_file_name = input("Name of the entry file :")
print ('\n')
if input_file_name == '':
   input_file_name = 'tsv_simple.tsv'
   
   
# read et transform the file tsv into a panda dataframe 
with open(input_file_name) :
    read_tsv = pd.read_csv(input_file_name, sep= '\t')
    tsv_to_df = pd.DataFrame(read_tsv)
    print(tsv_to_df)
    print ('\n')
    hyperlink_text = tsv_to_df.iloc[:,1]
    print(hyperlink_text)
    print ('\n')

      
# associate the hyperlink text with its category using the NLTK POS tagger
    text_tags = nltk.pos_tag(hyperlink_text)
    print('\n')
    print(text_tags)
   
# If in doubt for the meaning of a certain category, one can type in the console nltk.help.upenn_tagset('NN') to search what 'NN'means for example
    
   
# For every element of the column 'hyperlink_text' look inside it and tokenise its content 
    for line in hyperlink_text:
        print(line)
        line = re.sub(r'[^a-zA-Z0-9_\s]+', '', line) # we remove any special characters, while leaving numbers since NLTK has the special category 'CD' for numerals
        text_token = nltk.word_tokenize(line)
        print("the words in the hyperlink are" + str(text_token))
        print('\n')
        line =+ 1
        
      
# compute the proportion of structures
    categories = {'CC': 0, 'CD': 0, 'DT': 0, 'EX': 0, 'FW': 0, 'IN': 0, 'JJ': 0, 'JJR': 0, 'JJS': 0, 'LS': 0, 'MD': 0, 'NN': 0, 'NNS': 0, 'NNP': 0, 'NNPS': 0, 'PDT': 0, 'POS': 0, 'PRP': 0, 'PRP$': 0, 'RB': 0, 'RBR': 0, 'RBS': 0, 'RP': 0, 'TO': 0, 'UH': 0, 'VB': 0, 'VBD': 0, 'VBG': 0, 'VBN': 0, 'VBP': 0, 'VBZ': 0, 'WDT': 0, 'WP': 0, 'WP$': 0, 'WRB': 0}
    for text_tuple in text_tags: 
        tag_of_tuple = text_tags[text_tags.index(text_tuple)][1]
        categories[tag_of_tuple] += 1
    print(categories)
    
      
# remove from dictionnary all categories which are not instantiated in the hyperlinks 
    non_null_categories = {x:y for x,y in categories.items() if y!=0}
   
        
# create a pie chart showing the distribution of syntactic categories using matplotlib
    syntactic_category = non_null_categories.keys()
    frequence_of_syntactic_category = non_null_categories.values()
    plt.pie(frequence_of_syntactic_category, labels=syntactic_category, autopct='%1.1f%%')
    plt.title("Distribution of syntactic categories in hyperlinks")
    plt.show()
    
        
        
 
     
        
    
    



