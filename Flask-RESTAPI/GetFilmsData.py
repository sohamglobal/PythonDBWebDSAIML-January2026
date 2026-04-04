from flask import Flask
from pymongo import MongoClient

app=Flask(__name__)

# MongoDB Connectivity
client=MongoClient("mongodb+srv://praffull:mongodb913@sharayucluster.fib907c.mongodb.net/?appName=sharayucluster")
db=client['spiderdb']
coll=db['films']

@app.route('/films',methods=['GET'])
def getallfilms():
    films=list(coll.find())
    return films

@app.route('/films/genre/<genre>',methods=['GET'])
def searchfilms(genre):
    query={'category':genre}
    films=list(coll.find(query))
    return films

@app.route('/films/year/<year>',methods=['GET'])
def searchonyear(year):
    year=int(year)
    query={'releaseyr':year}
    print(query)
    films=list(coll.find(query))
    return films

if __name__=='__main__':
    app.run(debug=True)