import os

try:
    os.rename("praffull.txt","ethan.txt")
    print("file renamed")
except:
    print("not found")