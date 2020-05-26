
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
import re
import json

path = 'C:/Users/sheyu/Desktop/Cluster and Cloud Computing/Assign2/tweet_data'
keyword = 'chinese'
analyzer = SentimentIntensityAnalyzer()

def sentiment(fileList, keyword):
    score = []
    text_neutral = []
    text_positive = []
    text_negtive = []

    for file in fileList:
        with open(file, 'r') as f:
            data = json.load(f)
            for value in data.values():
                text = value['text']
                if bool(re.search(keyword, text, re.IGNORECASE)):
                    compoundScore = analyzer.polarity_scores(text)['compound']
                    score.append(compoundScore)

    print('The length is {}'.format(len(score)))
    score_ave = sum(score) / len(score)
    print('The average score is {:.4f}'.format(score_ave))
    score_positive = [x for x in score if x > 0.4]
    print('The number of positive is {}'.format(len(score_positive)))
    score_neutral = [x for x in score if -0.4 < x < 0.4]
    percent = len(score_positive) / len(score)
    print('The percentage of positive tweets is {:.2%}'.format(percent))
    return score


fileJan = []
fileFeb = []
fileMar = []
fileApr = []
for dir in os.listdir(path):
    dir_new = os.path.join(path, dir)

    stateFileByMonth = []

    for file in os.listdir(dir_new):
        filepath = os.path.join(dir_new, file)

        stateFileByMonth.append(filepath)
        filename = file.split('-')

        if filename[1] == '01':
            fileJan.append(filepath)
        elif filename[1] == '02':
            fileFeb.append(filepath)
        elif filename[1] == '03':
            fileMar.append(filepath)
        elif filename[1] == '04':
            fileApr.append(filepath)

    print('The sentiment statistical results of {} in {} are:'.format(keyword, dir))
    sentiment(stateFileByMonth, keyword)
    print()

totalFile = []
i = 0
for fileList in [fileJan, fileFeb, fileMar, fileApr]:
    i += 1
    totalFile += fileList
    print('Statistics data for month {} is:'.format(i))
    sentiment(fileList, keyword)
    print()

#sentiment(totalFile, keyword)


