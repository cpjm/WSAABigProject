from flask import Flask, jsonify, request, abort
from DAO import streamingshowsDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

#curl "http://127.0.0.1:5000/streamingshowss"
@app.route('/streamingshowss')
def getAll():
    #print("in getall")
    results = streamingshowsDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/streamingshowss/2"
@app.route('/streamingshowss/<int:id>')
def findById(id):
    foundstreamingshows = streamingshowsDAO.findByID(id)

    return jsonify(foundstreamingshows)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/streamingshowss
@app.route('/streamingshowss', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    streamingshows = {
        "title": request.json['title'],
        "author": request.json['author'],
        "price": request.json['price'],
    }
    addedstreamingshows = streamingshowsDAO.create(streamingshows)
    
    return jsonify(addedstreamingshows)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/streamingshowss/1
@app.route('/streamingshowss/<int:id>', methods=['PUT'])
def update(id):
    foundstreamingshows = streamingshowsDAO.findByID(id)
    if not foundstreamingshows:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'price' in reqJson and type(reqJson['price']) is not int:
        abort(400)

    if 'title' in reqJson:
        foundstreamingshows['title'] = reqJson['title']
    if 'author' in reqJson:
        foundstreamingshows['author'] = reqJson['author']
    if 'price' in reqJson:
        foundstreamingshows['price'] = reqJson['price']
    streamingshowsDAO.update(id,foundstreamingshows)
    return jsonify(foundstreamingshows)
        

    

@app.route('/streamingshowss/<int:id>' , methods=['DELETE'])
def delete(id):
    streamingshowsDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)