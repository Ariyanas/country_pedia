import requests
from bs4 import BeautifulSoup
import csv

URL = "https://en.wikipedia.org/wiki/States_and_union_territories_of_India"

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

table = soup.findAll('table', attrs={'class': 'wikitable'})
# tbody = table.tbody

# print(table)
i = 0
for tbl in table:
    print(i)
    print(tbl)
    i = i + 1

states = []

# for tr in tbody.findAll('tr'):
#     state = {}
#     th = tr.find('th')
#     tds = tr.findAll('td')

#     state['name'] = th
#     # state['capital'] = tds[2]

#     # print(tds)

#     states.append(state)

# print(states)

# states_file = '../results/indian_states.csv'

#print(countries)

# with open(country_file, 'w', newline='') as f:
#     wr = csv.DictWriter(f, ['name', 'isd', 'code', 'code_full'])
#     wr.writeheader()
#     for c in countries:
#         wr.writerow(c)
