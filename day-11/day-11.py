#day - 11
# python writing files (.txt , .json , .csv)
import os
file_path = "C:\\Users\\Axiri\\Developer\\Python-Learning\\day-11\\writing-files.txt"
file_data = "My name is Axirise"
file_data2 = ["I`m programer", "I learning python", "I like Pizza"]
with open(file_path, "w") as file:
   file.write(file_data + "\n")
   for data in file_data2:
      file.write(data + "\n")
   print("file.txt created is finished 👻")

import json
json_file = {
   "name" : "Axirise",
   "age" : "XX",
   "job" : "programer"
}
file_path = "C:\\Users\\Axiri\\Developer\\Python-Learning\\day-11\\writing-files.json"
with open(file_path, "w") as file:
   json.dump(json_file, file, indent= 4)
   print("file.json created is finished 👻")

import csv
file_path = "C:\\Users\\Axiri\\Developer\\Python-Learning\\day-11\\writing-files.csv"
csv_file = [["name","ID","job"],
            ["Axirise","3300","prgramer"],
            ["Rodjy", "3301", "programer"],
            ["Wassy","3302", "prgramer"]]
with open(file_path, "w") as file:
   writer = csv.writer(file)
   for row in csv_file:
      writer.writerows(row)
   print("file.csv created is finished 👻")

# python reading files (.txt , .json , .csv)
file_path = "C:\\Users\\Axiri\\Developer\\Python-Learning\\day-11\\writing-files.txt"
with open(file_path, "r") as file:
   contant = file.read(file)
   print(contant)

import json
file_path = "C:\\Users\\Axiri\\Developer\\Python-Learning\\day-11\\writing-files.json"
with open(file_path, "r") as file:
   contant = json.load(file)
   print(contant["name"])

import csv
file_path = "C:\\Users\\Axiri\\Developer\\Python-Learning\\day-11\\writing-files.csv"
with open(file_path, "r") as file:
   contant = csv.reader(file)
   for line in contant:
      print(line[0])

# python datetime 
import datetime
date = datetime.date(2026 , 7 , 19)
today = datetime.date.today()
time = datetime.time(9 , 5 ,1)
now = datetime.datetime.now()
now = now.strftime("%H : %M : %S --- %m - %d - %y")
print(now)
target_date = datetime.datetime(2026, 8, 1, 00, 00, 00)
current_date = datetime.datetime.now()
if target_date < current_date : 
   print("target date has passed") 
else:
   print("target date has not passed")

# python Alarm Clock
# i understand the idea