# testapi2.py
# This is a follow on from testapi.py
# As rapidapi limits the free requests daily, I have save dte JSON results in a file to use here.
# STEP 1 - run testapi.py and store the api results in a file.
# I used command line  ">" output redirection for this - see comments in testapi.py for more.
#
# in a json file, which can be read in here and processed.
# This will mean that testing/debugging/creating code will not use up the api limit.
#
import json

# code from 
# https://stackoverflow.com/questions/47659782/python-how-convert-single-quotes-to-double-quotes-to-format-as-json-string
#
# This is to fix teh incorrect JSON single quotes from the API tp double quotes
#
def correctSingleQuoteJSON(s):
    rstr = ""
    escaped = False

    for c in s:
    
        if c == "'" and not escaped:
            c = '"' # replace single with double quote
        
        elif c == "'" and escaped:
            rstr = rstr[:-1] # remove escape character before single quotes
        
        elif c == '"':
            c = '\\' + c # escape existing double quotes
   
        escaped = (c == "\\") # check for an escape character
        rstr += c # append the correct json
    
    return rstr

print("Opening file...")
# This file is the output of running "python testapi.py > testapi.log.json"
f = correctSingleQuoteJSON(open('testapi.log.json', 'r'))
#correctJson = correctSingleQuoteJSON(f)
print("File opened...")
print("Loading file into data object")
#data = json.load(f)
data = f
print("File loaded into data object")

#print("Closing file")
#f.close()
#print("File closed")

# using modified code based on
# https://stackoverflow.com/questions/73916163/looping-nested-json-object-in-python-to-collect-selected-fields-and-save-to-use
# 
for show in data:
    print(show)
    for genre in data[show]:
        genre_id = genre['id']
        genre_name = genre['name']
        print(genre_id, genre_name)