###########################################################################
#  INTERACTIVE PYTHON DICTIONARY
###########################################################################

import json
import difflib # library to compare text
from difflib import get_close_matches
data = json.load(open("data.json"))

###########################################################################
# FUNCTION TO GET DEFINITION OF A WORD
###########################################################################

def translate(word):
    word = word.lower()   # make program not case sensitive
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0: #checks for close matches
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no " % get_close_matches(word, data.keys())[0]) 
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The Word doesn't exist please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The Word doesn't exist please double check it."

############################################################################
# ASK USER FOR A WORD
############################################################################
word = input("Enter word: ")


############################################################################
# OUTPUT OF PROGRAM
############################################################################
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)