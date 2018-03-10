import json
import pandas as pd
import string

out =	{
		'business_id': [], 
		'name': [],
		'city': [],
		'stars': [],
		'review_count': [],
		'categories': [],
		'latitude': [],
		'longitude': [],
		}

with open('yelp_academic_dataset_business.json') as f:
	for line in f:
		j_content = json.loads(line)
		if j_content['city'] == 'Charlotte' or j_content['city'] == 'Pittsburgh':
			categoriesString = str(j_content['categories'])
			if categoriesString.find('Restaurants') != -1:
				print(j_content['city'])
				out['business_id'].append(j_content['business_id'])
				out['name'].append(j_content['name'])
				out['city'].append(j_content['city'])
				out['stars'].append(j_content['stars'])
				out['review_count'].append(j_content['review_count'])
				out['categories'].append(j_content['categories'])
				out['latitude'].append(j_content['latitude'])
				out['longitude'].append(j_content['longitude'])

df = pd.DataFrame(out)
df.to_csv('Extract_Business_IDs.csv', sep=',',encoding='utf-8')
