import os

try:
    os.rmdir("myprojects")
    print("directory removed")
except:
    print("directory not found")
