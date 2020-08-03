import requests
import json


url = "http://sihvm.southcentralus.cloudapp.azure.com:5000//api/v1.0/getPredData?city=kalijhora,WB"
to = "https://api.powerbi.com/beta/84c31ca0-ac3b-4eae-ad11-519d80233e6f/datasets/9cfcb897-2395-473d-acc2-4945ab5ef388/rows?key=5IhJpyyxCdk2%2B7rG7z0enA4UUq1Fh8cEy6XsR3BT%2FjhK%2FnEniJ0OL5T3t%2FLGZOAGaUg7XU8rYtF1a6sK4J6Dfg%3D%3D"

response = requests.get(url)

print(response)

data = response.text

print(type(data))

parsed = json.loads(data)

print(type(parsed))

#print(json.dumps(parsed, indent=4))

while True:
    for x in parsed:
        a = requests.post(to, json.dumps(x))
        print(a.text)
      













