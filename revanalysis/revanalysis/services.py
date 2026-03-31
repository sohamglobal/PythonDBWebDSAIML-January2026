from pymongo import MongoClient

class ReviewServices:
    def checkuserstatus(self,uid):
        client=MongoClient("mongodb+srv://praffull:mongodb913@sharayucluster.fib907c.mongodb.net/?appName=sharayucluster")
        db=client["ecomprojectdb"]
        coll=db["prousers"]
        user=coll.find_one({"userid":uid})
        print(user)
        return user
    
    def searchdocuments(self,f,v):
        dic={}
        dic[f]=v
        print(dic)
        client=MongoClient("mongodb+srv://praffull:mongodb913@sharayucluster.fib907c.mongodb.net/?appName=sharayucluster")
        db=client["ecomprojectdb"]
        coll=db["reviews"]
        data=list(coll.find(dic))
        return data