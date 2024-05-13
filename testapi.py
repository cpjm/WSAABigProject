import requests

url = "https://streaming-availability.p.rapidapi.com/shows/search/filters"

querystring = {"country":"ie","show_type":"movie","series_granularity":"show","order_by":"original_title","output_language":"en","order_direction":"asc","genres_relation":"and"}

headers = {
	"X-RapidAPI-Key": "48f6e1b26fmsh5e38f8360a33b4ep1e4ae5jsnd035d4a8a6e0",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# use encoding to avoid the following error
#File "C:\Users\Administrator\anaconda3\Lib\encodings\cp1252.py", line 19, in encode
#    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#UnicodeEncodeError: 'charmap' codec can't encode characters in position 144666-144669: character maps to <undefined>
print("Encoding>", response.encoding) # Prints: Encoding> utf-8
response.encoding = 'ISO-8859-1'
print(response.json())