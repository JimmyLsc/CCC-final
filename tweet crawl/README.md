# CCC-final

# 1. Crawl old tweets:

```
python crawl_history.py --loc='vic' --start='2020,5,1' --period=30 --max_query=10000 --sleep=60
```

loc: the location of the tweet  
start: the start date of the crawled tweet  
period: number of days to crawl  
max_query: maximum number of crawled tweet per day
sleep: program sleep time after crawling a day's tweets, it is measured in seconds

# 2. Crawl real time tweets:

```
python stream/stream.py
```

Running this program, it will constantly feed real time tweets into couchDB, check the settings in stream/config/json

# 3. Sentiment analysis:

```
python sentiment.py
```

It will predict sentiment for all tweets based on vaderSentiment.

# 4. format convertion:

```
python convert.py
```

Originally old tweets from each day are stored in a json, concentrate them into a big json based on continent.

# 5. analysis directory

Some analysis based on history tweets.