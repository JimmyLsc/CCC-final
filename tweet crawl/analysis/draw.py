import matplotlib.pyplot as plt
import json

input_file = ['2020-01.json', '2020-02.json', '2020-03.json', '2020-04.json']
vic_pos = []
vic_neg = []
north_pos = []
north_neg = []
queens_pos = []
queens_neg = []
south_pos = []
south_neg = []
west_pos = []
west_neg = []
nsw_pos = []
nsw_neg = []
tas_pos = []
tas_neg = []

for file in input_file:
	file = json.load(open(file))
	for state in file:
		if state[7:10] == 'nor':
			north_pos.append(file[state]['pos'] / file[state]['total'])
			north_neg.append(file[state]['neg'] / file[state]['total'])
		elif state[7:10] == 'vic':
			vic_pos.append(file[state]['pos'] / file[state]['total'])
			vic_neg.append(file[state]['neg'] / file[state]['total'])
		elif state[7:10] == 'que':
			queens_pos.append(file[state]['pos'] / file[state]['total'])
			queens_neg.append(file[state]['neg'] / file[state]['total'])
		elif state[7:10] == 'sou':
			south_pos.append(file[state]['pos'] / file[state]['total'])
			south_neg.append(file[state]['neg'] / file[state]['total'])
		elif state[7:10] == 'wes':
			west_pos.append(file[state]['pos'] / file[state]['total'])
			west_neg.append(file[state]['neg'] / file[state]['total'])
		elif state[7:10] == 'nsw':
			nsw_pos.append(file[state]['pos'] / file[state]['total'])
			nsw_neg.append(file[state]['neg'] / file[state]['total'])
		elif state[7:10] == 'tas':
			tas_pos.append(file[state]['pos'] / file[state]['total'])
			tas_neg.append(file[state]['neg'] / file[state]['total'])


def draw(pos=1):
	month = ['1', '2', '3', '4']
	if pos:
		plt.plot(month, vic_pos, color='red', label='Victoria')
		plt.plot(month, north_pos, color='violet', label='Northern')
		plt.plot(month, queens_pos, color='blue', label='Queensland')
		plt.plot(month, south_pos, color='yellow', label='Southern')
		plt.plot(month, west_pos, color='green', label='Western')
		plt.plot(month, nsw_pos, color='pink', label='New South Wales')
		plt.plot(month, tas_pos, color='olive', label='Tasmania')
		plt.title('Positive tweets percentage chart')
	else:
		plt.plot(month, vic_neg, color='red', label='Victoria')
		plt.plot(month, north_neg, color='violet', label='Northern')
		plt.plot(month, queens_neg, color='blue', label='Queensland')
		plt.plot(month, south_neg, color='yellow', label='Southern')
		plt.plot(month, west_neg, color='green', label='Western')
		plt.plot(month, nsw_neg, color='pink', label='New South Wales')
		plt.plot(month, tas_neg, color='olive', label='Tasmania')
		plt.title('Negative tweets percentage chart')
	plt.xlabel('month')
	plt.ylabel('percentage')
	plt.legend()
	plt.show()

draw(0)










