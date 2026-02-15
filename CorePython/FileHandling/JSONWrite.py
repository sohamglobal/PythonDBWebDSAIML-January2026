import json

data={
    "userid":"praffull",
    "username":"ethan hunt",
    "password":"chelsea786",
    "usertype":"student"
}

with open("user.json","w") as file:
    json.dump(data,file,indent=5)

with open("user.json","r") as file:
    data=json.load(file)
    print(data)
    #print(data["username"])