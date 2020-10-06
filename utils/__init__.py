import pymongo,re,json

with open("./auth.json",'r') as f:
    auth = json.load(f)

#Globals
client = pymongo.MongoClient(auth["mongo_url"])["Ame"]
Users = client["Users"]

def html_parse(text):
    text=re.sub(r'</?(b|B)>', '**', text)
    return re.sub(r'</?(i|I)>', '*', text)