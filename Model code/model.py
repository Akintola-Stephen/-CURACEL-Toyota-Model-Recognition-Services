from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://toyotanigeria.com/listings/rav4/'

page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
soup.find_all('img')
