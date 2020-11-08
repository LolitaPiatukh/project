import requests
import json

response = requests.get(
    ' http://www.nbrb.by/apihelp/exrates'
)
data = json.loads(response.text)
print(data)