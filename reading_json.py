import requests 
import json

# to start the localhost, place the required file in any folder an do the following command
# $ python -m http.server 8080
ministries_data = requests.get("http://localhost:8080/pak-fed-ministries.json")

print(json.loads(ministries_data.text))

# print(ministries_data.json())