# DAO - Data Access Object
# This is the project's data layer that handles the datbase connectivity.
# Author: Ciaran Moran
# Based on original code by Author: Andrew Beatty
import mysql.connector
import dbconfig as cfg
class streamingshowsDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''

    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self):
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def getAll(self):
        cursor = self.getcursor()
        sql="select id, my_review, my_ratepercent, my_recommend_yn  from streamingshows"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))

        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="select id, my_review, my_ratepercent, my_recommend_yn from streamingshows where id = %s"
        values = (id)
        #values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def create(self, id, streamingshows):
        #cursor = self.getcursor()
        #sql="insert into streamingshows (my_review,my_ratepercent,my_recommend_yn) values (%s,%s,%s)"
        #values = (streamingshows.get("my_review"), streamingshows.get("my_ratepercent"), streamingshows.get("my_recommend_yn"))
        #cursor.execute(sql, values)
        #self.connection.commit()
        #newid = cursor.lastrowid
        #streamingshows["id"] = newid
        #self.closeAll()
        #return streamingshows
        cursor = self.getcursor()
        sql="update streamingshows set my_review= %s,my_ratepercent=%s, my_recommend_yn=%s  where id = %s"
        print(f"update streamingshows {streamingshows}")
        values = (streamingshows.get("my_review"), streamingshows.get("my_ratepercent"), streamingshows.get("my_recommend_yn"),id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()


    def update(self, id, streamingshows):
        cursor = self.getcursor()
        sql="update streamingshows set my_review= %s,my_ratepercent=%s, my_recommend_yn=%s  where id = %s"
        print(f"update streamingshows {streamingshows}")
        values = (streamingshows.get("my_review"), streamingshows.get("my_ratepercent"), streamingshows.get("my_recommend_yn"),id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        cursor = self.getcursor()
        # Here the record won't physically be deleted.
        # Rather the record needs to be updated, as the user review info
        # is on the same record as the API show info.
        # So therefore the review fields are updated with blanks
        # ie they are blanked out.
        #sql="delete from streamingshows where id = %s"
        sql="update streamingshows set my_review="",my_ratepercent="", my_recommend_yn=""  where id = %s"
        values = (id)
        #values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()

        print("delete done")

    def convertToDictionary(self, resultLine):
        attkeys=['id','my_review','my_ratepercent', "my_recommend_yn"]
        streamingshows = {}
        currentkey = 0
        for attrib in resultLine:
            print("attrib:", attrib," currentkey:",currentkey)
            streamingshows[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1
        return streamingshows

streamingshowsDAO = streamingshowsDAO()