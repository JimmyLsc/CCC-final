import couchdb
import json
import os

db = couchdb.Server('http://admin:admin@localhost:5984')

path = '/data/data/'

keys = ['southern', 'western', 'vic', 'nsw', 'tas', 'queens']

for key in keys:
    error = 0
    filenames = os.listdir(path + 'output_'+key)
    for filename in filenames:
        with open(path + 'output_'+key+'/' + filename, encoding='utf-8') as f:
            tweets = json.load(f)
        count = 0
        tweet_list = []
        for _, tweet in tweets.items():
            try:
                tweet_list.append(tweet)
                count += 1
                if count % 5000 == 0:
                    db[key].update(tweet_list)
                    tweet_list = []
                    count = 0
            except:
                error += 1
                if error >=5:
                    os._exit()
        if count != 0:
            try:
                db[key].update(tweet_list)
            except:
                error += 1
                if error >=5:
                    os._exit()
