import json
import os


path = '../output'
file = ['2020-01', '2020-02', '2020-03', '2020-04']


for month in file:
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
		for date_data in os.listdir(state_path):
			if not date_data.startswith('2020'):
				continue
			if date_data.startswith(month):
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
		print (p)
		print (dic)
		dic_all[p] = dic
	dic_all = json.dumps(dic_all)
	with open(os.path.join(month+'.json'), 'w') as fr:
		fr.write(dic_all)


















