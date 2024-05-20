# WSAABigProject
WSAA Big Project CRUD Web Application

HOSTED: https://cpjm.eu.pythonanywhere.com/viewer.html
Was working with DB, then I made a change(?!) and now tonight it's broken!
And of course I made the fatal mistake of trying to fix it on pythonanywhere using the online editor there.

API
Here I decided to use RAPID API.
I've never used it before but found it via a Google (never!).
Rapid API has a multitude of collections of many different APIs for different topics etc sports, food etc.
I choose the movie/tv show API (liek IMDB) from 
https://rapidapi.com/movie-of-the-night-movie-of-the-night-default/api/streaming-availability/


Anyhow for the solution I managed to create a MySQL and import in the data from the API.
This was done via the mySQL command line, and copy/paste of a create command.
The mySQL data creation scriupt was created using WAMPSERVER/phpMyAdmin which I installed on my laptop.

streaming_shows.sql - see thus for a sample of the data I pulled from the API.

API to MySQL
Step 1 - python testapi.py
    Input: rapid-api 
    Output: testapi.json 
    This will read from rapid-api and will pull down movie/tv show DB as per IMDB.
    It will save the JSON to a file.
    As the RAPID-API has limits on the number of requests, the file acts liek a cache.

Step 2 - python jsontomysql.py
    Input: testapi.json
    Output: creates table streaming movies and populates the data
    This program will read the API data from the file and creates the rows on the mySQL DB using the API data.

Step 3 - viewer.html
use to to view/maintain the move/tv show data
Basically the movie data is supplemented with the additional fields I added:- 
  my_review - text entery of your review of the movie/tv show
  my_ratepercent - the percent you give the program
  my_recommend_yn - do I recommend it Y/N
The viewer.html inputs these 3 "review" fields from the user and stores it on the DB as supplemental 
information for each movie/tv show.

Other:-
server.py - the flask routing
DAO.py - the data object for interfacing with the DB
requirements.txt - python packages required
