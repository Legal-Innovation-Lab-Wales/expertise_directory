import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import re


def get_colleges():

	URL = 'https://www.swansea.ac.uk/staff/'
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')

	colleges = soup.find(class_='contextual-nav')



	# URL = 'https://www.swansea.ac.uk/staff/'
	# page = requests.get(URL)
	# soup = BeautifulSoup(page.content, 'html.parser')
	# colleges = {}
	# colleges['name'] = []
	# colleges['url'] = []
	#
	# college_names = soup.find_all(class_='su-image-heading')
	# for college_name in college_names:
	# 	college_name = college_name.text.strip()
	# 	print(college_name)
	# 	colleges['name'].append(college_name)
	#
	# college_images = soup.find_all(class_='su-image')
	# for college_image in college_images:
	# 	college_url = college_image.find('a')['href']
	# 	college_url = re.sub('^.+staff/', '', college_url)
	# 	college_url = college_url.replace('/', '')
	# 	print(college_url)
	# 	colleges['url'].append(college_url)
	#
	# print(colleges)


def get_staff(college):

	URL = 'https://www.swansea.ac.uk/staff/' + college
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')

	jsondata[college] = []

	staff_all = soup.find(class_='contextual-nav')
	staff_in_list = staff_all.find_all('li')
	for staff in staff_in_list:
		staff_url = staff.find('a')['href']
		name_and_aoe_list = get_name_and_aoe_list(staff_url)

		if name_and_aoe_list:
			jsondata[college].append(name_and_aoe_list)


def get_name_and_aoe_list(staff_url):

	URL = 'https://www.swansea.ac.uk/' + staff_url
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')

	staff_member = {}
	expertise = []

	name = soup.find(class_='staff-profile-overview-honorific-prefix-and-full-name')
	if name:
		name = name.text.strip()
		# print(name)

	aoe_list = soup.find(class_='staff-profile-areas-of-expertise')
	if aoe_list:
		# add to dict
		staff_member['name'] = name
		staff_member['url'] = URL

		# remove html
		aoe_list = aoe_list.ul.text.strip()
		# remove line breaks
		aoe_list = aoe_list.replace("\n", ", ").strip()
		# add to dict
		staff_member['expertise'] = aoe_list

		return staff_member


jsondata = {}

jsondata['last_update'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print('Getting Staff Details')

# get_colleges()
get_staff('law')
# print (jsondata)

print('Save Output File')
with open('new-expertise.json', 'w', encoding='utf-8') as file:
	json.dump(jsondata, file, ensure_ascii=False, indent=4)
