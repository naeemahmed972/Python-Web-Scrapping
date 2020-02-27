import csv
from pak_fed_ministries_data import get_ministries_data

ministries = get_ministries_data()

with open('./pak-fed-ministries.csv', 'w+', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Name of Ministry', 'Link to Ministry'])

    for ministry in ministries:
        writer.writerow([ministry['text'], ministry['link']])
        # print(ministry['text'])