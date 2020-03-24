import json
import pymongo 

myclient = pymongo.MongoClient("160.40.52.130:27017")

mydb = myclient["dependabilityToolbox"]
mycollection = mydb["securityAssessment"]

with open('imd-technical-debt-updated.json') as json_file:
    data = json.load(json_file)
	
    
    print(data['projects'])
	
mycollection.insert_many(data["projects"])