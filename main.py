import requests
import json

def region_contracts(region_code):
    url=f"http://openapi.clearspending.ru/restapi/v3/contracts/search/?customerregion={region_code}"
    data = requests.get(url).json()
    return data

result = region_contracts(78)
#print(result)

with open("result.json", "w") as json_file:
    json.dump(result, json_file)