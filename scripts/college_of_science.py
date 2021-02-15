from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
from scrape_expertise import scrape_staff

url_prefix = 'https://www.swansea.ac.uk/staff/science/'

def get_department_staff(department):
	url = url_prefix + department
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	return {
		'key': department,
		'name': department,
		'staff': scrape_staff(department, url_prefix, soup.find('table'))
	}

def get_staff():
	college = {
		'key': 'college_of_science',
		'name': 'College Of Science',
		'departments': []
	}

	with ThreadPoolExecutor() as executor:
		futures = []
		for department in ['biosciences', 'chemistry', 'compsci', 'geography', 'maths', 'physics']:
			futures.append(executor.submit(get_department_staff, department))

		for future in futures:
			college['departments'].append(future.result())

	return college
