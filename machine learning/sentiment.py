from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
import os

analyzer = SentimentIntensityAnalyzer()
path = 'history'
output = 'output1'
for p in os.listdir(path):
	if not p.startswith('output_'):
		continue
	state_path = os.path.join(path, p)
	for date_data in os.listdir(state_path):
		if not date_data.startswith('2020'):
			continue
		# print (date_data)
		data = json.load(open(os.path.join(state_path, date_data), encoding='utf-8'))
		for i in range(len(data.keys())):
			sentence = data['t'+str(i)]['text']
			sentiment = analyzer.polarity_scores(sentence)
			if sentiment['compound'] >= 0.5:
				data['t'+str(i)]['label'] = 1
			elif sentiment['compound'] <= -0.5:
				data['t'+str(i)]['label'] = -1
			else:
				data['t'+str(i)]['label'] = 0
		data = json.dumps(data)
		with open(os.path.join(path, output, p, date_data), 'w') as fr:
			fr.write(data)


