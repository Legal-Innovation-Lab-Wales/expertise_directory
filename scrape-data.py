import requests
from bs4 import BeautifulSoup




def get_name_and_aoe_list():

	URL = 'https://www.swansea.ac.uk/staff/law/barazza-s/'
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')


	name = soup.find(class_='staff-profile-overview-honorific-prefix-and-full-name')
	aoe_list = soup.find(class_='staff-profile-areas-of-expertise')

	print(name.text.strip())
	print(aoe_list.ul.text.strip())


get_name_and_aoe_list()
