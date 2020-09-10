import requests
from bs4 import BeautifulSoup

def get_colleges():

	URL = 'https://www.swansea.ac.uk/staff/'
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')

	college_names = soup.find_all(class_='su-image-heading')
	for college_name in college_names:
		print(college_name.text.strip())

	college_images = soup.find_all(class_='su-image')
	for college_image in college_images:
		college_url = college_image.find('a')['href']
		print(college_url)


def get_staff(college):

	URL = 'https://www.swansea.ac.uk/staff/' + college
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')

	staff_all = soup.find(class_='contextual-nav')
	staff_in_list= staff_all.find_all('li')
	for staff in staff_in_list:
	 	staff_url = staff.find('a')['href']
	 	print (staff_url)







def get_name_and_aoe_list(staff_url):

	URL = 'https://www.swansea.ac.uk/' + staff_url
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')


	name = soup.find(class_='staff-profile-overview-honorific-prefix-and-full-name')
	aoe_list = soup.find(class_='staff-profile-areas-of-expertise')

	print(name.text.strip())
	print(aoe_list.ul.text.strip())


get_staff('law')
