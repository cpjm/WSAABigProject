from flask import Flask, jsonify, request, abort
from DAO import streamingshowsDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

#curl "http://127.0.0.1:5000/streamingshows"
@app.route('/streamingshows')
def getAll():
    #print("in getall")
    results = streamingshowsDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/streamingshows/2"
@app.route('/streamingshows/<int:id>')
def findById(id):
    foundstreamingshows = streamingshowsDAO.findByID(id)

    return jsonify(foundstreamingshows)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/streamingshows
@app.route('/streamingshows', methods=['POST'])
def create():

    if not request.json:
        abort(400)
    # other checking
    streamingshows = {
        "title": request.json['title'],
        "overview": request.json['overview'],
        "genres_name": request.json['genres_name']
        "streamingOptions_ie_service_name": request.json['streamingOptions_ie_service_name'],
        "my_review": request.json['my_review'],
        "my_ratepercent": request.json['my_ratepercent'],
        "my_recommend_yn": request.json['my_recommend_yn']
    }
    addedstreamingshows = streamingshowsDAO.create(streamingshows)

    return jsonify(addedstreamingshows)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/streamingshowss/1
@app.route('/streamingshows/<int:id>', methods=['PUT'])
def update(id):
    foundstreamingshows = streamingshowsDAO.findByID(id)
    if not foundstreamingshows:
        abort(404)

    if not request.json:
        abort(400)
    reqJson = request.json
    #if 'my_recommend_yn' in reqJson and type(reqJson['my_recommend_yn']) is not int:
    #    abort(400)

    if 'title' in reqJson:
        foundstreamingshows['title'] = reqJson['title']
    if 'overview' in reqJson:
        foundstreamingshows['overview'] = reqJson['overview']
    if 'genres_name' in reqJson:
        foundstreamingshows['genres_name'] = reqJson['genres_name']
    if 'streamingOptions_ie_service_name' in reqJson:
        foundstreamingshows['streamingOptions_ie_service_name'] = reqJson['streamingOptions_ie_service_name']
    if 'my_review' in reqJson:
        foundstreamingshows['my_review'] = reqJson['my_review']
    if 'my_ratepercent' in reqJson:
        foundstreamingshows['my_ratepercent'] = reqJson['my_ratepercent']
    if 'my_recommend_yn' in reqJson:
        foundstreamingshows['my_recommend_yn'] = reqJson['my_recommend_yn']
    streamingshowsDAO.update(id,foundstreamingshows)
    return jsonify(foundstreamingshows)




@app.route('/streamingshows/<int:id>' , methods=['DELETE'])
def delete(id):
    streamingshowsDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)