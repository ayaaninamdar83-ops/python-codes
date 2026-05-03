import json
import csv

try:
    with open('data.json',"r")as Sarthak:
        data = json.load(Sarthak)


    print("csv file created successfully")

except FileNotFoundError:
    print("file not found")

except PermissionError:
    print("i do not have permission to access file")

