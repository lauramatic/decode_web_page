import requests
from bs4 import BeautifulSoup
import sys

base_url = 'http://www.getjoan.com'
r = requests.get(base_url)
print(r)
if r.status_code != 200:
    print("Url not available")
    sys.exit()
print(r.text)
