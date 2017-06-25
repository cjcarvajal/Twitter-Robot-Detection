import pymongo
import json

file_path = {path to the file with the tweets you want to load}

def loadFile():
	with open(file_path) as data_file:
		file_str = data_file.read()
		file_str = '[' + file_str + ']'
		file_str = file_str.replace('}{','},{')
		return json.loads(file_str)

client = pymongo.MongoClient()
db = client.twitter_robots

tweets = loadFile()
for batch in tweets:
	for status in batch['statuses']:
		db.tweets.insert_one(status)
	
