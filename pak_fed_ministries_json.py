import json
from pak_fed_ministries_data import get_ministries_data

ministries = get_ministries_data()

print(json.dumps(ministries, indent=4))

with open('./pak-fed-ministries.json', 'w+') as json_file:
    json.dump(ministries, json_file, indent=4)