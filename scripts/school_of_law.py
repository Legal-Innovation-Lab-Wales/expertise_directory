from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
from scrape_expertise import scrape_staff

url = 'https://www.swansea.ac.uk/staff/law'

def get_department_staff(soup, department):
	section = soup.find('div',{'id':'{}-contents'.format(department)})

	return {
		'key': department,
		'name': department,
		'staff': scrape_staff(department, url, section.find('table'))
	}

def get_staff():
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	college = {
		'key': 'hrc_school_of_law',
		'name': 'Hillary Rodham Clinton School Of Law',
		'departments': []
	}

	with ThreadPoolExecutor() as executor:
		futures = []
		for department in ['law', 'criminology']:
			futures.append(executor.submit(get_department_staff, soup, department))

		for future in futures:
			college['departments'].append(future.result())

	return college