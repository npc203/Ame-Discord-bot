import datetime
import requests,json
r=json.loads(requests.get("https://official-joke-api.appspot.com/random_joke").text)
print(type(r["setup"]))
print(r["punchline"])
