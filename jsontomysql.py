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
        file.close()

        # newfilename=""
        # newfilename=filename+".new"
        # print("newfilename", newfilename)
        # input("Paused...")

        #https://stackoverflow.com/questions/19007404/valid-json-in-text-file-but-python-json-loads-gives-json-object-could-be-decode
        # json_newfile = open(newfilename, 'w')
        # json_oldfile = open(filename, 'r')
        # old_data = json_oldfile.read()
        # json.dump(old_data, json_newfile)
        # json_newfile.close()
        # json_oldfile.close()

        #with open(filename, 'r', encoding='utf-8') as file:
        #with open(filename, 'r', encoding=encoding) as file:
        with open(filename, 'r') as file:
            print("1> ")
            # Read the file content and replace single quotes with double quotes
            
            #file_content = file.read() #.replace("'", "\"")
            
            # Load the JSON data
            print("2> ")
            #print(file_content[0:500])
            data = json.load(file)
            print("3> ")

        # data=[]
        # with open(filename, 'r', encoding='utf-8') as file:
        #     print("1> ")
        #     # Read the file content and replace single quotes with double quotes
        #     #data = json.load(file) 
            
        #     for line in file:
        #          data.append(json.loads(line))
            
            # print("3> ")

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

    
    #print("len(data)>",len(data))
    #input("Pending len(data)...")

    for line in data['shows']:
 
        # iniatialise the strings
        # just in case we get an error setting from the JSON
        # due to bad or missing data.
        id=""
        imdbId=""
        tmdbId=""
        title=""
        overview=""
        releaseYear=""
        genres_name=""
        directors=""
        cast=""
        rating="" 
        imageSet_horizontalPoster_w480=""
        streamingOptions_ie_service_name="" 
        streamingOptions_ie_service_imageSet_lightThemeImage="" 
        streamingOptions_ie_type=""
        streamingOptions_ie_link=""
        streamingOptions_ie_quality=""
        streamingOptions_ie_price_formatted=""    


        # here I am using try and using it to ignore (pass) any errors whilst processing the JSON data  
        # this will help bypass any bad data that could be in the JSON api feed        
        print("=========")
        #print("line:",line)
        imdbIdnew=line['imdbId'] #['itemType'][0] #['show']#[0]['imdbId']
        print(imdbIdnew)
        #input("Paused.................................................................") 
        print("=========")

        try: 
            imdbId=line['imdbId']
            print(imdbId) 
        except: pass
        try: 
            tmdbId=line['tmdbId'] 
            print(tmdbId) 
        except: pass
        try: 
            title = line['title'] 
            print(title) 
        except: pass
        try: 
            overview=line['overview'] 
            print(overview) 
        except: pass
        try: 
            releaseYear=line['releaseYear']
            print(releaseYear) 
        except: pass
        try: 
            genres_name=line['genres'][0]['name']
            print(genres_name) 
        except: pass
        try: 
            directors=line['directors'] 
            print(directors) 
        except: pass
        try: 
            cast=line['cast'] 
            print(cast) 
        except: pass
        try: 
            rating=line['rating']
            print(rating) 
        except: pass
        try: 
            imageSet_horizontalPoster_w480=line['imageSet']['horizontalPoster']['w480']
            print(imageSet_horizontalPoster_w480) 
        except: pass
        try: 
            streamingOptions_ie_service_name=line['streamingOptions']['ie'][0]['service']['name']
            print(streamingOptions_ie_service_name) 
        except: pass
        try: 
            streamingOptions_ie_service_imageSet_lightThemeImage=line['streamingOptions']['ie'][0]['service']['imageSet']['lightThemeImage']
            print(streamingOptions_ie_service_imageSet_lightThemeImage) 
        except: pass
        try: 
            streamingOptions_ie_type=line['streamingOptions']['ie'][0]['type']
            print(streamingOptions_ie_type)
        except: pass
        try: 
            streamingOptions_ie_link=line['streamingOptions']['ie'][0]['link']
            print(streamingOptions_ie_link)
        except: pass
        try: 
            streamingOptions_ie_quality=line['streamingOptions']['ie'][0]['quality']
            print(streamingOptions_ie_quality)
        except: pass
        try: 
            streamingOptions_ie_price_formatted=line['streamingOptions']['ie'][0]['price']['formatted']
            print(streamingOptions_ie_price_formatted)    
        except: pass

        print("----------------------------------------------------------------------")
        print("----------------------------------------------------------------------")
        try:
            print("Before writing to DB, pausing...",(title, genres_name, releaseYear),end="")
            #input()
            cursor.execute("INSERT INTO streaming_shows (title, genre, year) VALUES (%s, %s, %s)", (title, genres_name, releaseYear))
            print("After writing to DB, pausing...",(title, genres_name, releaseYear),end="")
            #input()
        except: pass

        #input("Loop pause...")

    #input("Pending after i loop...")

    # print(data['shows'][0]['id']) 
    # print(data['shows'][0]['imdbId']) 
    # print(data['shows'][0]['tmdbId']) 
    # print(data['shows'][0]['title']) 
    # print(data['shows'][0]['overview']) 
    # print(data['shows'][0]['releaseYear']) 
    # print(data['shows'][0]['genres'][0]['name']) 
    # print(data['shows'][0]['directors']) 
    # print(data['shows'][0]['cast']) 
    # print(data['shows'][0]['rating']) 
    # print(data['shows'][0]['imageSet']['horizontalPoster']['w480']) 
    # print(data['shows'][0]['streamingOptions']['ie'][0]['service']['name']) 
    # print(data['shows'][0]['streamingOptions']['ie'][0]['service']['imageSet']['lightThemeImage']) 
    # print(data['shows'][0]['streamingOptions']['ie'][0]['type'])
    # print(data['shows'][0]['streamingOptions']['ie'][0]['link'])
    # print(data['shows'][0]['streamingOptions']['ie'][0]['quality'])
    # print(data['shows'][0]['streamingOptions']['ie'][0]['price']['formatted'])    
    # input("Pending [0]...")


    # Below is working code
    # print(data['shows'][0]['id']) 
    # print(data['shows'][0]['imdbId']) 
    # print(data['shows'][0]['tmdbId']) 
    # print(data['shows'][0]['title']) 
    # print(data['shows'][0]['overview']) 
    # print(data['shows'][0]['releaseYear']) 
    # print(data['shows'][0]['genres'][0]['name']) 
    # print(data['shows'][0]['directors']) 
    # print(data['shows'][0]['cast']) 
    # print(data['shows'][0]['rating']) 
    # print(data['shows'][0]['imageSet']['horizontalPoster']['w480']) 
    # print(data['shows'][0]['streamingOptions']['ie'][0]['service']['name']) 
    # print(data['shows'][0]['streamingOptions']['ie'][0]['service']['imageSet']['lightThemeImage']) 
    # print(data['shows'][0]['streamingOptions']['ie'][0]['type'])
    # print(data['shows'][0]['streamingOptions']['ie'][0]['link'])
    # print(data['shows'][0]['streamingOptions']['ie'][0]['quality'])
    # print(data['shows'][0]['streamingOptions']['ie'][0]['price']['formatted'])    
    # input("Pending [0]...")

    # print(data['shows'][1]['id']) 
    # print(data['shows'][1]['imdbId']) 
    # print(data['shows'][1]['tmdbId']) 
    # print(data['shows'][1]['title']) 
    # print(data['shows'][1]['overview']) 
    # print(data['shows'][1]['releaseYear']) 
    # print(data['shows'][1]['genres'][0]['name']) 
    # print(data['shows'][1]['directors']) 
    # print(data['shows'][1]['cast']) 
    # print(data['shows'][1]['rating']) 
    # print(data['shows'][1]['imageSet']['horizontalPoster']['w480']) 
    # print(data['shows'][1]['streamingOptions']['ie'][0]['service']['name']) 
    # print(data['shows'][1]['streamingOptions']['ie'][0]['service']['imageSet']['lightThemeImage']) 
    # print(data['shows'][1]['streamingOptions']['ie'][0]['type'])
    # print(data['shows'][1]['streamingOptions']['ie'][0]['link'])
    # print(data['shows'][1]['streamingOptions']['ie'][0]['quality'])
    # print(data['shows'][1]['streamingOptions']['ie'][0]['price']['formatted'])    
    # input("Pending [1]...")



    # Insert data into the table
    # for show in data:
    #     print("6> ")
    #     print("show:",show[0])
    #     print("7> ")
    #     title = show.get('title')
    #     print("8> ")
    #     genre = show.get('genre')
    #     print("9> ")
    #     year = show.get('year')
    #     print("10> ")
    #     cursor.execute("INSERT INTO streaming_shows (title, genre, year) VALUES (%s, %s, %s)", (title, genre, year))
    #     print("11> ")

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    filename = "testapi.json"
    data = read_json_file(filename)
    
    if data:
        save_to_database(data)
