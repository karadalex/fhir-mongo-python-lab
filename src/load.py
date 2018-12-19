import os
import json
from pymongo import MongoClient


client = MongoClient('mongodb://root:example@localhost:27017/')
db = client.fhir
fhir = db.fhir

os.chdir('./data')
for file in os.listdir(os.getcwd()):
    if file.endswith(".json"):
        with open(file) as json_data:
            # Convert file to python object
            resource = json.load(json_data)
            resource_id = fhir.insert_one(resource).inserted_id
            print(file + " " + str(resource_id))

print("Loaded FHIR resources successfully")
