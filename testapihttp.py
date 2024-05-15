# To run this test I execute the code and output to a log file.
# This facilitates a quick output to a file for inspection afterwards.
# e.g. python testapi.py > testapi.log
# I can then open this using Notepad++, and use plugin > JasonTools > Pretty-print current json file
# and this produces a more readable format, which is useful for working out what info/fields are returned.
#
import http.client
import json

url = "https://streaming-availability.p.rapidapi.com/shows/search/filters"

querystring = {"country":"ie","show_type":"movie","series_granularity":"show","order_by":"original_title","output_language":"en","order_direction":"asc","genres_relation":"and"}

headers = {
	"X-RapidAPI-Key": "48f6e1b26fmsh5e38f8360a33b4ep1e4ae5jsnd035d4a8a6e0",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

conn = http.client.HTTPSConnection("streaming-availability.p.rapidapi.com")
conn.request("GET", "/shows/search/filters?country=ie&show_type=movie&series_granularity=show&order_by=original_title&output_language=en&order_direction=asc&genres_relation=and", headers=headers)

r = conn.getresponse()
#data = res.read()

#print(data.decode("utf-8"))

# Write large data to a file in chunks
my_data = json.loads(r.json())
# my_data is a dict mapping the JSON

with open('testapihttp.json', 'w') as f:
    json.dump(my_data, f)