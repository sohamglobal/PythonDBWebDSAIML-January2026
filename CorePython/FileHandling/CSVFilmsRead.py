import csv

with open("films.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)


with open("films.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row['Name'],row['Actor'])