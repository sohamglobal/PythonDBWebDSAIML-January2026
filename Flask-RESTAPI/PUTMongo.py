from flask import Flask, request, jsonify
from pymongo import MongoClient

app=Flask(__name__)

# MongoDB Connectivity
client=MongoClient("mongodb+srv://praffull:mongodb913@sharayucluster.fib907c.mongodb.net/?appName=sharayucluster")
db=client['ecomprojectdb']
coll=db['prousers']

@app.route('/users/modify/<userid>',methods=['PUT'])
def update_users(userid):
    data=request.get_json()

    if not data:
        return jsonify({"error":"No data received"}),400
    
    result=coll.update_one(
        {"userid":userid},
        {"$set":data}
    )

    if result.matched_count==0:
        return jsonify({"error":"User not found"}),404
    
    return jsonify({
        "message":"User data modified successfully",
        "userid":userid
    })
    

app.run(debug=True)