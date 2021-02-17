import concurrent.futures
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import string
import re

# Scrape the staff from a departments table - this code can be shared between SOL and COS but not COAH
def scrape_staff(department, url, table):
	staff_data = []
	rows = table.find_all('tr')

	with tqdm(total = len(rows)) as progressbar:
		progressbar.set_description('Processing {} department aoe'.format(department))

		with concurrent.futures.ThreadPoolExecutor() as executor:
			futures = {executor.submit(scrape_expertise, url, row.find_all('td')[0]): row for row in rows}

			for future in concurrent.futures.as_completed(futures):
				staff_member = future.result()
				progressbar.update(1)

				if staff_member:
					staff_data.append(staff_member)

	return staff_data

# Scrape the expertise from a staff members page
def scrape_expertise(url_prefix, list_item):
	link = list_item.find('a')
	staff_member = {}

	if link is not None:
		href = link.get('href')

		if href.startswith('http') or href.startswith('/'):
			staff_url = href if href.startswith('http') else url_prefix + href
			page = requests.get(staff_url)
			soup = BeautifulSoup(page.content, 'html.parser')

			name = soup.find(class_='staff-profile-overview-honorific-prefix-and-full-name')

			if name:
				name = name.text.strip()

			aoe_list = soup.find(class_='staff-profile-areas-of-expertise')

			if aoe_list:
				expertise = []
				staff_member['name'] = name
				staff_member['url'] = staff_url

				for area in aoe_list.find_all('li'):
					text = area.text
					text = text.replace('* ', '')  # Some staff have an odd bullet point character in their AOE
					text = text.replace(',', '')
					text = text.replace(';', '')
					text = text.replace('•', '')
					text = text.strip()
					text = re.sub('^-', '', text)
					text = string.capwords(text)

					expertise.append(text)

				staff_member['expertise'] = expertise

	return staff_member