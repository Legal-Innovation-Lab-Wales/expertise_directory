import concurrent.futures
import requests
from bs4 import BeautifulSoup
from scrape_expertise import get_expertise
from tqdm import tqdm

url_domain = 'https://www.swansea.ac.uk'
url_prefix = url_domain + '/staff/arts-and-humanities/'

def get_department_staff(department):
	link = department.find('a')
	url = url_domain + link.get('href')
	name = link.text.replace(' Staff', '')
	key = url.replace(url_prefix, '').replace('-', '_').replace('/', '')

	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	staff_data = []
	list_items = soup.find('div', class_='order-last').find('ul').find_all('li')

	with tqdm(total = len(list_items)) as progressbar:
		progressbar.set_description('Processing {} department aoe'.format(key))

		with concurrent.futures.ThreadPoolExecutor() as executor:
			futures = {executor.submit(get_expertise, url_domain, list_item): list_item for list_item in list_items}

			for future in concurrent.futures.as_completed(futures):
				staff_member = future.result()
				progressbar.update(1)

				if staff_member:
					staff_data.append(staff_member)

	return {
		'key': key,
		'name': name,
		'staff': staff_data
	}

def get_staff():
	page = requests.get(url_prefix)
	soup = BeautifulSoup(page.content, 'html.parser')

	college = {
		'key': 'college_of_arts_and_humanities',
		'name': 'College of Arts & Humanities',
		'departments': []
	}

	with concurrent.futures.ThreadPoolExecutor() as executor:
		futures = []
		for department in soup.find('ul', class_='contextual-nav').find_all('li'):
			futures.append(executor.submit(get_department_staff, department))

		for future in futures:
			college['departments'].append(future.result())

	return college