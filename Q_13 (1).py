# cOpy data from json file to csv file
import json
import csv

try:
    with open('data.json',"r")as Sarthak:
        data = json.load(Sarthak)

    with open('data.csv', 'w', newline='') as csv_file:
        
        writer = csv.writer(csv_file)
        
        writer.writerow(data[0].keys())
        
        for row in data:
            writer.writerow(row.values())

    print("csv file created successfully")

except FileNotFoundError:
    print("file not found")