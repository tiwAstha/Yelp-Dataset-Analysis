import json
import pandas as pd
from collections import OrderedDict
dataframe = pd.read_csv('Chinese_businessID.csv')
businesses= [] 
for index, row in dataframe.iterrows():
		businesses.append(row['business_id'])


review = open('E:\School\sem2\Data Science\hw02\yelp_dataset_challenge_round9\yelp_academic_dataset_review.json')
review_list = []
print("start")
for r in review:
   rj = json.loads(r)
   if rj['business_id'] in businesses:
       review_list.append(rj['text'])
       

print(len(rj['business_id']))
textFile = open('chinesereviews.txt', 'w')
print("start")
for item in review_list:
    print item
    textFile.write(str(item))

print("done")
textFile.close()
