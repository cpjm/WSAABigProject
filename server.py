from flask import Flask, jsonify, request, abort
from DAO import streaming_showsDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

#curl "http://127.0.0.1:5000/streaming_shows"
@app.route('/streaming_shows')
def getAll():
    #print("in getall")
    results = streaming_showsDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/streaming_shows/2"
@app.route('/streaming_shows/<int:id>')
def findById(id):
    foundstreaming_shows = streaming_showsDAO.findByID(id)

    return jsonify(foundstreaming_shows)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/streaming_shows
@app.route('/streaming_shows', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    streaming_shows = {
        "my_review": request.json['my_review'],
        "my_ratepercent": request.json['my_ratepercent'],
        "my_recommend_yn": request.json['my_recommend_yn'],
    }
    addedstreaming_shows = streaming_showsDAO.create(streaming_shows)
    
    return jsonify(addedstreaming_shows)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/streaming_showss/1
@app.route('/streaming_shows/<int:id>', methods=['PUT'])
def update(id):
    foundstreaming_shows = streaming_showsDAO.findByID(id)
    if not foundstreaming_shows:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'my_recommend_yn' in reqJson and type(reqJson['my_recommend_yn']) is not int:
        abort(400)

    if 'my_review' in reqJson:
        foundstreaming_shows['my_review'] = reqJson['my_review']
    if 'my_ratepercent' in reqJson:
        foundstreaming_shows['my_ratepercent'] = reqJson['my_ratepercent']
    if 'my_recommend_yn' in reqJson:
        foundstreaming_shows['my_recommend_yn'] = reqJson['my_recommend_yn']
    streaming_showsDAO.update(id,foundstreaming_shows)
    return jsonify(foundstreaming_shows)
        

    

@app.route('/streaming_shows/<int:id>' , methods=['DELETE'])
def delete(id):
    streaming_showsDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)