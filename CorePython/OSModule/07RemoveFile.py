import os

try:
    os.remove("unwanted.json")
    print("file removed")
except:
    print("not found")