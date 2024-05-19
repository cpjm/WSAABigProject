# testapi.py (STAGE 1 of 2)
# Input: https://streaming-availability.p.rapidapi.com/shows/search/filters
# Output: testapi.json
#
# This python program reads information in from the API web service.
# The API provies a JSON response.
# It then writes the json data to a file called testapi.json.
# The API is from rapidapi.com
# This particular API contains movie/cinema info that mirrors IMDB.
# Info of the web page for the service can be read at:- 
# https://rapidapi.com/movie-of-the-night-movie-of-the-night-default/api/streaming-availability/pricing
#
# Initially to run this test I executed the code and output to a log file.
# The program contained many different print statements to assist with debugging.
# This facilitates a quick output to a file for inspection afterwards.
# e.g. python testapi.py > testapi.log
# Additionally I can open the JSON file using Notepad++, and use plugin > JasonTools > Pretty-print current json file
# and this produces a more readable format of the JSON fields/info.
#
# 2 Stage process explained.
# The reason behind the 2 stages/programs is due to usage limits on the API itself.  
# STAGE 1 (testapi.py) - read the API JSON and write to the JSON file.
# STAGE 2 (jsontomysql.py) - Then the second program can be run multiple times on the file.
#   Therefore the file copy acts like a cached version of the API JSON. 
#   This facilitates more debugging and testing without breaching the API access limits.
#
# jsontomysql.py (STAGE 2)
# NOTE - A second "stage 2" program exists called jsontomysql.py
# This program exists to read the JSON file and write the info to the MySQL DB.
#
#
import requests
import json

url = "https://streaming-availability.p.rapidapi.com/shows/search/filters"

querystring = {"country":"ie","show_type":"movie","series_granularity":"show","order_by":"original_title",\
               "output_language":"en","order_direction":"asc","genres_relation":"and"}

headers = {
	"X-RapidAPI-Key": "48f6e1b26fmsh5e38f8360a33b4ep1e4ae5jsnd035d4a8a6e0",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

# use encoding to avoid the following error
#File "C:\Users\Administrator\anaconda3\Lib\encodings\cp1252.py", line 19, in encode
#    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#UnicodeEncodeError: 'charmap' codec can't encode characters in position 144666-144669: character maps to <undefined>
#print("Encoding>", response.encoding) # Prints: Encoding> utf-8
#response.encoding = 'ISO-8859-1'
#
#print(response.json())
#with open('testapi.json', 'w',encoding="utf-8") as f:
#        # Write the content of the response to the file
#        #f.write(str(response.content))
#        json.dump(response,f,ensure_ascii=False)

# Write large data to a file in chunks
#my_data = json.loads(r.json())
# my_data is a dict mapping the JSON

r = requests.get(url, headers=headers, params=querystring)
data = r.json()
#s1 = json.dumps(r.json())
#d2 = json.loads(s1)
print("len(data):",str(len(data)))
input("Pausing...")

with open('testapi.json', 'w') as f:
    json.dump(data, f)
    #for line in data["shows"]:
    #    f.write(json.dumps(line) + "\n")

f.close()
