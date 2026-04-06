from flask import Flask, request, jsonify
from pymongo import MongoClient

app=Flask(__name__)

# MongoDB Connectivity
client=MongoClient("mongodb+srv://praffull:mongodb913@sharayucluster.fib907c.mongodb.net/?appName=sharayucluster")
db=client['sohamdb']
coll=db['students']

@app.route('/student/add',methods=['POST'])
def add_student():
    data=request.get_json()
    result=coll.insert_one(data)
    return jsonify({
        'message':'new student added',
        'id':str(result.inserted_id)
    })

app.run(debug=True)