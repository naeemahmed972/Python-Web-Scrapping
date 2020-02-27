import requests
from bs4 import BeautifulSoup

def get_ministries_data():
    html = requests.get('http://www.pakistan.gov.pk/').text 
    soup_obj = BeautifulSoup(html, 'lxml')

    fed_ministries = soup_obj.findAll('div', {'id':'link1'})

    def ministry_to_dict(ministry):
        ministry_link = ministry.find('a')
        link_data = dict()
        try:
            link_data['text'] = ministry_link.text.strip()
        except KeyError:
            link_data['text'] = "No Text"
        try:
            link_data['link'] = ministry_link.attrs['href']
        except KeyError:
            link_data['link'] = "No href"
        return link_data
    
    ministries_data = [ministry_to_dict(ministry) for ministry in fed_ministries]

    return ministries_data

if __name__ == "__main__":
    print(get_ministries_data())
