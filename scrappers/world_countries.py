import requests
from bs4 import BeautifulSoup
import csv

URL = "https://countrycode.org"

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

table = soup.find('table')
tbody = table.tbody

countries = []

for tr in tbody.findAll('tr'):
    country = {}
    tds = tr.findAll('td')

    country['name'] = tds[0].a.text
    country['isd'] = tds[1].text

    code  = tds[2].text
    country['code'] = code[0:2]
    country['code_full'] = code[5:]
    
    countries.append(country)

country_file = '../results/countries.csv'

#print(countries)

with open(country_file, 'w', newline='') as f:
    wr = csv.DictWriter(f, ['name', 'isd', 'code', 'code_full'])
    wr.writeheader()
    for c in countries:
        wr.writerow(c)

