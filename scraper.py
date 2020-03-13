import requests
from bs4 import BeautifulSoup

# Enter the amazon URL below
URL = ''

# Enter your user agent here 'Search google for My User Agent'
headers = {}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()

print(title.strip())