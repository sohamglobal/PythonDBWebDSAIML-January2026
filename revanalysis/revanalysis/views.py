from django.shortcuts import render
from pymongo import MongoClient

def homepage(request):
    return render(request,"index.html")

def register(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")

def newreview(request):
    return render(request,"newreview.html")

def adduser(request):
    if request.method=="POST":
        uid=request.POST.get("userid")
        ps=request.POST.get("password")
        nm=request.POST.get("name")
        gn=request.POST.get("gender")
        mo=request.POST.get("mobile")
        client=MongoClient("mongodb+srv://praffull:mongodb913@sharayucluster.fib907c.mongodb.net/?appName=sharayucluster")
        db=client["ecomprojectdb"]
        coll=db["prousers"]
        dic={}
        dic['userid']=uid
        dic['password']=ps
        dic['username']=nm
        dic['gender']=gn
        dic['mobile']=mo
        try:
            coll.insert_one(dic)
            sts="success"
        except:
            sts="failed"

    return render(request,"reguserstatus.html",{'status':sts})

def addreview(request):
    if request.method=="POST":
        # receive the data
        # put it in a dictionary
        # insert in mongodb collection

    return render(request,"addrevstatus.html",{'status':sts})
    