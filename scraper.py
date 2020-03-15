import requests
from bs4 import BeautifulSoup
import smtplib

# Enter the amazon URL below
URL = ''

# Enter your user agent here 'Search google for My User Agent'
headers = {}

def check_price():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="priceblock_ourprice").get_text()
	converted_price = float(price[0:5])

	if(converted_price < ): # Enter the price drop after which you want to be notifed
	    send_mail()

	print(converted_price)
	print(title.strip())

	if(converted_price < ): # Enter the price drop after you want to be notifed
	    send_mail()


def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('', '')

	subject = 'Price fell down!'
	body = 'Check the Amazon link '

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
		'',
		'',
		msg
	)
	print('HEY EMAIL HAS BEEN SENT!')

	server.quit()


check_price()

