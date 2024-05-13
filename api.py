import requests
import apiconfig as cfg
import json

url = "https://food-recipes-with-images.p.rapidapi.com/"

querystring = {"q":"chicken soup"}

headers = {
	"X-RapidAPI-Key":  cfg.rapidapi['key'],
	"X-RapidAPI-Host":  cfg.rapidapi['host']
}

# The service api call is working.
# however due to a limit on daily calls for the free acount
# I have saved the response json to a file using Notepad++
#   - using copy and paste
#   - and then JsonTools plugin > pretty-print to re-format json into readable format
# And this file can then be used as many times as required.

#response = requests.get(url, headers=headers, params=querystring)
#print(response.json())

# This json open file  statement made with the help of
# https://stackoverflow.com/
# https://stackoverflow.com/questions/28171696/python-json-to-csv-bad-encoding-unicodedecodeerror-charmap-codec-cant-dec
# 
jfile="api-response-example.json"
with open(jfile, 'r', encoding="cp866") as json_file:
    data = json.load(json_file)
    #    for key, value in data.items():
    #        with open(f'{key}.json', 'w') as f:
    #            json.dump(value, f, indent=4)    
    #print(data)

    #for key, value in data.items():
    #    with open(f'{key}.json', 'w') as f:
    #        json.dump(value, f, indent=4)    

with open(jfile, 'r', encoding="cp866") as file:
        for line in file:
            j = json.loads(line)
            json.dump(j)
