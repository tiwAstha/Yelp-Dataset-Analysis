
import pandas as pd
from collections import OrderedDict
import json

city = 'Pittsburgh'
print("Finding results for " + city)

dataframe = pd.read_csv('Extract_Business_IDs.csv')

businesses = {
	'business_id': [], 
	'city': [],
	'categories': [],
	}

for index, row in dataframe.iterrows():
	if row['city'] == city:
		businesses['business_id'].append(row['business_id'])
		businesses['city'].append(row['city'])
		businesses['categories'].append(row['categories'])

CategoriesAndCountsMap = {};
	
for element in businesses['categories']:
	element = element.replace("[", "");
	element = element.replace("]", "");
	tokens = element.split(',');
	for elem in tokens:
		elem = elem.strip();
		isFound = CategoriesAndCountsMap.get(elem);
		if isFound == None:
			CategoriesAndCountsMap[elem] = 1;
		else:
			CategoriesAndCountsMap[elem] = isFound + 1;
			
	
sortedCategoriesAndCountsMap = OrderedDict(sorted(CategoriesAndCountsMap.items(), key=lambda x: x[1]))

output = open('restaurant_categories_count_' + city + '.txt', 'w')
for k,v in sortedCategoriesAndCountsMap.items():
	output.write(k + ":" + str(v) + "\n")
output.close()

sortedCategoriesAndCountsMap.clear();
CategoriesAndCountsMap.clear();

with open('yelp_academic_dataset_checkin.json') as f:
	for line in f:
		j_content = json.loads(line)
		try:	
			indexOfIdInListOfBusinesses = businesses['business_id'].index(j_content['business_id']);	
			cats = businesses['categories'][indexOfIdInListOfBusinesses];
			cats = cats.replace("[", "");
			cats = cats.replace("]", "");
			tokens = cats.split(',');
			for elem in tokens:
				elem = elem.strip();
				isFound = CategoriesAndCountsMap.get(elem);
				if isFound == None:
					CategoriesAndCountsMap[elem] = 1;
				else:
					CategoriesAndCountsMap[elem] = isFound + 1;
		except ValueError:
			pass

sortedCategoriesAndCountsMap = OrderedDict(sorted(CategoriesAndCountsMap.items(), key=lambda x: x[1]))
output = open('category_checkins_count' + city + '.txt', 'w')
for k,v in sortedCategoriesAndCountsMap.items():
	output.write(k + ":" + str(v) + "\n")
output.close()
