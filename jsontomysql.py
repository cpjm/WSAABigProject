import json
import mysql.connector
import chardet # $ pip install chardet
# from https://stackoverflow.com/questions/32311824/parsing-complex-json-with-python
# pip install simplejson
import simplejson as json 


def read_json_file(filename):
    try:
        # from https://stackoverflow.com/questions/13590749/reading-unicode-file-data-with-bom-chars-in-python
        # detect file encoding
        with open(filename, 'rb') as file:
            raw = file.read(32) # at most 32 bytes are returned
            encoding = chardet.detect(raw)['encoding']
            print("Encoding>", encoding)

        with open(filename, 'r', encoding='utf-8') as file:
            print("1> ")
            # Read the file content and replace single quotes with double quotes
            file_content = file.read() #.replace("'", "\"")
            # Load the JSON data
            print("2> ")
            print(file_content[0:500])
            data = json.loads(file_content)
            print("3> ")
            return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.decoder.JSONDecodeError:
        print(f"Error: File '{filename}' is not in valid JSON format or is empty.")
        return None

def save_to_database(data):
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="streamingshows"
    )
    cursor = conn.cursor()

    # Create table if not exists
    print("4> ")
    cursor.execute("CREATE TABLE IF NOT EXISTS streaming_shows (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), genre VARCHAR(255), year INT)")
    print("5> ")

    #cnt=0
    #for attribute, value in data.items():
    #    print("attribute>",attribute) # example usage
    #    print("value>",value) # example usage
    #    print("CNT...........................................................................", cnt)
    #input("Pending...")

    
    print(data['shows'][0]['id']) 
    print(data['shows'][0]['imdbId']) 
    print(data['shows'][0]['tmdbId']) 
    print(data['shows'][0]['title']) 
    print(data['shows'][0]['overview']) 
    print(data['shows'][0]['releaseYear']) 
    print(data['shows'][0]['genres'][0]['name']) 
    print(data['shows'][0]['directors']) 
    print(data['shows'][0]['cast']) 
    print(data['shows'][0]['rating']) 
    print(data['shows'][0]['imageSet']['horizontalPoster']['w480']) 
    print(data['shows'][0]['streamingOptions']['ie'][0]['service']['name']) 
    print(data['shows'][0]['streamingOptions']['ie'][0]['service']['imageSet']['lightThemeImage']) 
    print(data['shows'][0]['streamingOptions']['ie'][0]['type'])
    print(data['shows'][0]['streamingOptions']['ie'][0]['link'])
    print(data['shows'][0]['streamingOptions']['ie'][0]['quality'])
    print(data['shows'][0]['streamingOptions']['ie'][0]['price']['formatted'])    
    input("Pending outside loop...")


    # Insert data into the table
    for show in data:
        print("6> ")
        print("show:",show[0])
        print("7> ")
        title = show.get('title')
        print("8> ")
        genre = show.get('genre')
        print("9> ")
        year = show.get('year')
        print("10> ")
        cursor.execute("INSERT INTO streaming_shows (title, genre, year) VALUES (%s, %s, %s)", (title, genre, year))
        print("11> ")

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    filename = "testapi.json"
    data = read_json_file(filename)
    if data:
        save_to_database(data)
