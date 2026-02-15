import csv

data=[
    ['Name','Relyear','Genre','Actor'],
    ['The Matrix',1999,'Action','Keanu Reeves'],
    ['Sholay',1975,'Action','Amitabh Bachchan'],
    ['Dil se',1998,'Romance','Shah Rukh Khan']
]

with open("films.csv","w",newline='') as file:
    writer=csv.writer(file)
    writer.writerows(data)