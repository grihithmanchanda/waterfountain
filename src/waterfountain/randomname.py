from codecs import getencoder
import os
import requests

#need to set environment variable for api key
API_KEY = os.environ["API_KEY"]

gender = input("Type m for a male name and f for a female name: ")

if gender == "m":
    gender = "f"
else:
    gender = "m"

payload = {
    "key": API_KEY,
    "gender": gender,
    "usage": "eng",
    "number": 1
}

response = requests.get("https://www.behindthename.com/api/random.json", params=payload)
res = response.json()

print(res["names"][0])
