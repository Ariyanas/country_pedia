import requests
from bs4 import BeautifulSoup
import csv

URL = ""

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
