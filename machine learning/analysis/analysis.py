import json
import os
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet, stopwords
import operator

sign = ['.', ',', '?', '!', '#', ':', '’', '@', '…', "'s", 'https', "n't", '&', '...', ')', '-', '(', "''"]
stopword = stopwords.words('english') + sign
keyword = [wordnet.synset('china.n.01'), wordnet.synset('chinese.n.01')]
lemmatizer = WordNetLemmatizer()

def find_similar(texts, n=20):
	dic = defaultdict(int)
	res = []
	for text in texts:
		tokens = nltk.word_tokenize(text.lower())
		tokens_pos = nltk.tag.pos_tag(tokens)
		for token, pos in tokens_pos:
			if not pos.startswith('NN'):
				continue
			if token in stopword:
				continue
			word = lemmatizer.lemmatize(token, 'n')
			max_similairty = 0
			for synset in wordnet.synsets(word,'n'):
				for k in keyword:
					similarity = synset.wup_similarity(k)
					if similarity > max_similairty:
						max_similairty = similarity
			dic[word] = max(max_similairty, dic[word])
	sort_list = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
	for i in range(n):
		res.append(sort_list[i][0])
	return res


def find_commonest(texts, n=20):
	dic = defaultdict(int)
	res = []
	for text in texts:
		tokens = nltk.word_tokenize(text.lower())
		for token in tokens:
			if token in stopword:
				continue
			dic[token] += 1
	sort_list = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
	for i in range(n):
		res.append(sort_list[i][0])
	return res




path = 'output'
dic_all = {}
for p in os.listdir(path):
	if not p.startswith('output'):
		continue
	state_path = os.path.join(path, p)
	dic = {}
	pos = 0
	neg = 0
	neutral = 0
	total = 0
	china_count = 0
	texts = []
	for date_data in os.listdir(state_path):
		if not date_data.startswith('2020'):
			continue
		data = json.load(open(os.path.join(state_path, date_data), encoding='utf-8'))
		for i in range(len(data.keys())):
			label = data['t'+str(i)]['label']
			if label == 1:
				dic['pos'] = dic.get('pos', 0) + 1
			elif label == -1:
				dic['neg'] = dic.get('neg', 0) + 1
			else:
				dic['neutral'] = dic.get('neutral', 0) + 1
			dic['total'] = dic.get('total', 0) + 1
			if 'china' in data['t'+str(i)]['text']:
				dic['china_count'] = dic.get('china_count', 0) + 1
			texts.append(data['t'+str(i)]['text'])
	top_similar = find_similar(texts)
	commonest = find_commonest(texts)
	dic['top_similar'] = top_similar
	dic['commonest'] = commonest
	print (p)
	print (dic)
	dic_all[p] = dic
dic_all = json.dumps(dic_all)
with open(os.path.join('frequency.json'), 'w') as fr:
	fr.write(dic_all)


















