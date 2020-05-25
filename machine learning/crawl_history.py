import GetOldTweets3 as got
import datetime
import time
import json
import os
import argparse
from urllib import error


parser = argparse.ArgumentParser(description='history tweet')
parser.add_argument('--loc', type=str, default='vic')
parser.add_argument('--start', type=str, default='2020,1,1')
parser.add_argument('--period', type=int, default=130)
parser.add_argument('--max_query', type=int, default=10000)
parser.add_argument('--sleep', type=int, default=60)


args = parser.parse_args()
loc = args.loc
if loc == 'vic':
	location = '-37.7,144.9'
	within = '250km'
elif loc == 'nsw':
	location = '-31.9,147.1'
	within = '380km'
elif loc == 'tas':
	location = '-42.0,146.7'
	within = '120km'
elif loc == 'queens':
	location = '-22.6,145.1'
	within = '700km'
elif loc == 'northern':
	location = '-19.3,133.3'
	within = '500km'
elif loc == 'southern':
	location = '-30.3,135.3'
	within = '500km'
elif loc == 'western':
	location = '-30.0,121.6'
	within = '750km'

start = args.start.split(',')
start_year = int(start[0])
start_month = int(start[1])
start_day = int(start[2])

if not os.path.exists('output_'+loc):
	os.mkdir('output_'+loc)

date_start = datetime.datetime(start_year, start_month, start_day)
date_until = datetime.datetime(start_year, start_month, start_day+1)

start_string = date_start.strftime("%Y-%m-%d")
until_string = date_until.strftime("%Y-%m-%d")

lang = 'en'
max_tweets = args.max_query

for i in range(args.period):
	try:
		dic = {}
		i = 0
		tweetCriteria = got.manager.TweetCriteria()\
						.setSince(start_string)\
						.setUntil(until_string)\
						.setMaxTweets(max_tweets)\
						.setNear(location)\
						.setWithin(within)\
						.setLang(lang)
		print('--- Starting query... ---')
		tweets = got.manager.TweetManager.getTweets(tweetCriteria)

		print('--- Writing JSON... ---')
		for t in tweets:
			if not t.text.startswith('RT'):
				dic['t'+str(i)] = {}
				dic['t'+str(i)]['id'] = t.id
				dic['t'+str(i)]['username'] = t.username
				dic['t'+str(i)]['date'] = str(t.date)
				dic['t'+str(i)]['text'] = t.text
				i += 1
			
		print ('dict length: ', len(dic.keys()))
		dic = json.dumps(dic)
		with open('output_'+loc+'/'+start_string+'.json', 'w') as fr:
			fr.write(dic)

		print('--- Going to sleep... ---\n\n')
		time.sleep(args.sleep)
		print (start_string)
		date_start += datetime.timedelta(days=1)
		date_until += datetime.timedelta(days=1)
		start_string = date_start.strftime("%Y-%m-%d")
		until_string = date_until.strftime("%Y-%m-%d")
	except Exception as e:
		print ('mistake happen:')
		print (e)
