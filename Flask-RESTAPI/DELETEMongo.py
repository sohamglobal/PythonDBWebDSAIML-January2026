from flask import Flask, request, jsonify
from pymongo import MongoClient

app=Flask(__name__)

# MongoDB Connectivity
client=MongoClient("mongodb+srv://praffull:mongodb913@sharayucluster.fib907c.mongodb.net/?appName=sharayucluster")
db=client['ecomprojectdb']
coll=db['prousers']

@app.route("/users/delete/<userid>",methods=['DELETE'])
def delete_user(userid):
    result=coll.delete_one({"userid":userid})
    if result.deleted_count==0:
        return jsonify({"error":"user not found"}),404
    
    return jsonify({
        "message":"user deleted successfully",
        "userid":userid
    })

app.run(debug=True)