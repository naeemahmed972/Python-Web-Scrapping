# In this program, we extract the links for all Pakistan Federal Ministries
# From the website: http://www.pakistan.gov.pk/

import requests
from bs4 import BeautifulSoup

def get_fed_ministries(url):
    req = requests.get(url)

    soup_obj = BeautifulSoup(req.text, 'lxml')

    # fed_ministries = soup_obj.find('div', {'id':'col1_inner'}).findAll('a')
    fed_ministries = soup_obj.findAll('div', {'id':'link1'})

    # for ministry in fed_ministries:
    #     print(f"{ministry.text}: {ministry.attrs['href']}")
    #     # print(ministry.text)
    #     # print(ministry.attrs['href'])

    for ministry in fed_ministries:
        ministry_link = ministry.find('a')
        try:
            print(f"{ministry_link.text}: {ministry_link.attrs['href']}")
        except KeyError:
            print("Key Error: No 'href' attribute for the link.")

get_fed_ministries('http://www.pakistan.gov.pk/')