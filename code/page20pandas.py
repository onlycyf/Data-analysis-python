import pandas as pd
from pymongo import MongoClient

# a = pd.read_csv('./youtube_video_data/US_video_data_numbers.csv')
# print(a)

client = MongoClient()
collection = client['douban']['tv1']
data = list(collection.find())

print(data)
