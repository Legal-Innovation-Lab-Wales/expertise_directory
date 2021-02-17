from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
from scrape_expertise import scrape_staff

url_domain = 'https://www.swansea.ac.uk'
url_prefix = url_domain + '/staff/science/'

def get_department_staff(department):
	link = department.find('a')
	url = url_domain + link.get('href')
	name = link.text.replace('Our ', '').replace(' Staff', '').replace(' staff', '')
	key = url.replace(url_prefix, '').replace('-', '_').replace('/', '')

	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	return {
		'key': key,
		'name': name,
		'staff': scrape_staff(key, url_prefix, soup.find('table'))
	}

def get_staff():
	page = requests.get(url_prefix)
	soup = BeautifulSoup(page.content, 'html.parser')

	college = {
		'key': 'college_of_science',
		'name': 'College of Science',
		'departments': []
	}

	with ThreadPoolExecutor() as executor:
		futures = []
		for department in soup.find('ul', class_='contextual-nav').find_all('li'):
			futures.append(executor.submit(get_department_staff, department))

		for future in futures:
			college['departments'].append(future.result())

	return college
