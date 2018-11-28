import requests
from bs4 import BeautifulSoup
import csv

URL = ""

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

table = soup.find('table')
tbody = table.tbody

countries = []

for tr in tbody.findAll('tr'):
    country = {}
    tds = tr.findAll('td')

    country['name'] = tds[0].a.text

    code  = tds[2].text
    country['code'] = code[0:2]
    country['code_full'] = code[5:]

    country['isd'] = tds[1].text
    
    countries.append(country)

country_file = 'countries.csv'

print(countries)

with open(country_file, 'w', newline='') as f:
    wr = csv.DictWriter(f,['name','code','code_full','isd'])
    wr.writeheader()
    for c in countries:
        wr.writerow(c)

