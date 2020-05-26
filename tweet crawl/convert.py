import json
import os

path = 'output'
for p in os.listdir(path):
	if not p.startswith('output'):
		continue
	state_path = os.path.join(path, p)
	dic = {}
	k = 0
	for date_data in os.listdir(state_path):
		if not date_data.startswith('2020'):
			continue
		data = json.load(open(os.path.join(state_path, date_data), encoding='utf-8'))
		for i in range(len(data.keys())):
			dic['t'+str(k)] = data['t'+str(i)]
			k += 1
	dic = json.dumps(dic)
	with open(os.path.join('new/'+p+'.json'), 'w') as fr:
		fr.write(dic)