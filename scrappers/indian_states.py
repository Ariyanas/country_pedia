import requests
from bs4 import BeautifulSoup
import csv

URL = "https://simple.wikipedia.org/wiki/States_and_territories_of_India"

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

tables = soup.findAll('table', attrs={'class': 'wikitable'})

states = []

tbody_state = tables[0].find('tbody')

for tr in tbody_state.findAll('tr')[1:]:
    tds = tr.findAll('td')
    state = {}

    state['name'] = tds[0].a.text
    state['capital'] = tds[1].text
    state['code'] = tds[2].text[0:2]

    states.append(state)

states_file = '../results/indian_states.csv'

with open(states_file, 'w', newline='') as f:
    wr = csv.DictWriter(f, ['name', 'capital', 'code'])
    wr.writeheader()
    wr.writerows(states)