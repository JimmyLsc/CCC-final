import json
import TwitterAPI
import database
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

with open('./config.json', encoding='utf-8') as f:
	data = json.load(f)

api_key = data['api_key']
api_secret = data['api_secret']
access_key = data['access_key']
access_secret = data['access_secret']
url = data['url']
locations = data['locations']

api = TwitterAPI.TwitterAPI(api_key, api_secret, access_key, access_secret)
db = database.Couchdb(url)
analyzer = SentimentIntensityAnalyzer()

def extract(tweet):
	if 'text' not in tweet or tweet['text'].startswith('RT'):
		return None
	if 'place' not in tweet or 'full_name' not in tweet['place']:
		return None
	location = tweet['place']['full_name']
	if 'Queensland' in location:
		db_name = 'queens'
	elif 'New South Wales' in location:
		db_name = 'nsw'
	elif 'Victoria' in location:
		db_name = 'vic'
	elif 'Western Australia' in location:
		db_name = 'western'
	elif 'South Australia' in location:
		db_name = 'southern'
	elif 'North' in location:
		db_name = 'northern'
	else:
		return None
	db_data = {}
	if 'id' in tweet:
		db_data['id'] = tweet['id']
	if 'user' in tweet and 'name' in tweet['user']:
		db_data['username'] = tweet['user']['name']
	if 'created_at' in tweet:
		db_data['date'] = tweet['created_at']
	db_data['text'] = tweet['text']
	db_data['label'] = sentiment(tweet['text'])
	return db_data, db_name


def sentiment(text):
	sentiment = analyzer.polarity_scores(text)
	if sentiment['compound'] >= 0.5:
		return 1
	elif sentiment['compound'] <= -0.5:
		return -1
	else:
		return 0

count = 0
location_filter = {}
location_filter['locations'] = locations
while True:
	try:
		results = api.request('statuses/filter', location_filter)
		for tweet in results:
			db_data, db_name = extract(tweet)
			if db_data:
				db.upload(db_data, db_name)
				print (db_data)
				count += 1
				if count % 100 == 0:
					print (count)
	except:
		print ('crawl error.')













