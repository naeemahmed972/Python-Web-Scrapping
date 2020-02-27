import requests 
import csv

# to start the localhost, place the required file in any folder an do the following command
# $ python -m http.server 8080
ministries_data = requests.get("http://localhost:8080/pak-fed-ministries.csv").text

ministries = ministries_data.split('\n')

reader = list(csv.reader(ministries, delimiter=',', quotechar='"'))

lines = [line for line in reader[:-1]]

for line in lines:
    print(line)