import pymongo

with open("./url.txt",'r') as f:
    url = f.read()

#Globals
client = pymongo.MongoClient(url)["Ame"]
Users = client["Users"]