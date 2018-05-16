# import libraries
import requests
from bs4 import BeautifulSoup

# insert the webpage you want to parse
URL = 'https://www.getjoan.com'
the_word = 'joan'
r = requests.get(URL, allow_redirects=False)
soup = BeautifulSoup(r.content, 'html.parser')

#Find by a specific word
words = soup.find(text=lambda text: text and the_word in text)
print(words)








