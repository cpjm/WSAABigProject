# To run this test I execute the code and output to a log file.
# This facilitates a quick output to a file for inspection afterwards.
# e.g. python testapi.py > testapi.log
# I can then open this using Notepad++, and use plugin > JasonTools > Pretty-print current json file
# and this produces a more readable format, which is useful for working out what info/fields are returned.
#
import requests
import json

url = "https://streaming-availability.p.rapidapi.com/shows/search/filters"

querystring = {"country":"ie","show_type":"movie","series_granularity":"show","order_by":"original_title","output_language":"en","order_direction":"asc","genres_relation":"and"}

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

with open('testapi.json', 'w') as f:
    json.dump(data, f)
