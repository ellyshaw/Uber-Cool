import urllib.request
import json
import pymongo
from pprint import pprint
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

url = r'REDDITLINK/.json?limit=500'
analyser = SentimentIntensityAnalyzer()
comments = {}
with urllib.request.urlopen(url) as uber:
    content = uber.read()
contentd = json.loads(content)
for u in contentd[1]['data']['children']:
        comments[u['data']['id']] = analyser.polarity_scores(u['data']['body'])['compound']

import matplotlib.pyplot as plt
%pylab inline
plt.figure()
import plotly.plotly as py
from plotly.graph_objs import *
trace1 = Scatter(
    x = list(comments.keys()),
    y = list(comments.values())
)
data = [trace1]

py.plot(data, filename = 'comments')

c = pymongo.MongoClient("mongodb://localhost")
db = c.uber
coll = db.reddituber
coll.insert(comments)
