from concurrent.futures import ThreadPoolExecutor
import json
from datetime import datetime
from school_of_law import get_staff as get_law_staff
from college_of_science import get_staff as get_cos_staff
from college_of_arts_and_humanities import get_staff as get_coah_staff

json_data = {}
json_data['last_update'] = datetime.now().strftime("%H:%M %d-%m-%Y")
json_data['colleges'] = []

with ThreadPoolExecutor() as executor:
	futures = []
	for college in [get_law_staff, get_cos_staff, get_coah_staff]:
		futures.append(executor.submit(college))

	for future in futures:
		json_data['colleges'].append(future.result())

with open('../public/expertise.json', 'w', encoding='utf-8') as file:
	json.dump(json_data, file, ensure_ascii=False, indent=4)
