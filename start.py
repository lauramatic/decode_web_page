import requests
from bs4 import BeautifulSoup

base_url = 'http://www.getjoan.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
