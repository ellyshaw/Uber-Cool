
# coding: utf-8

# In[1]:


cd ..


# In[2]:


cd Documents\getoldtweets


# In[3]:


import got3 as got
import urllib.request
from datetime import datetime, timedelta
from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


startdate = datetime.strptime('2012-01-01', '%Y-%m-%d')
enddate = datetime.strptime('2017-11-12', '%Y-%m-%d')


# In[5]:


daterange=enddate-startdate
days = daterange.days


# In[6]:


days


# In[7]:


tweets = []


# In[8]:


for i in range(days):
    
    mod_date = startdate + timedelta(days=i)
    mod_date1 = startdate + timedelta(days=i+1)
    str_date = mod_date.strftime("%Y-%m-%d")
    str_date1 = mod_date1.strftime("%Y-%m-%d")
    try:
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch("uber london").        setSince(str_date).setUntil(str_date1).setMaxTweets(250)

        for t in got.manager.TweetManager.getTweets(tweetCriteria):
            print(t.date)
            l = {}
            l["Text"]= t.text
            l["Date"]= t.date
            l["Retweets"]= t.retweets
            l["Favourites"]= t.favorites
            tweets.append(l)
    except:
        print('error')
            


# In[14]:


for s in tweets:
    print(s["Text"])


# In[9]:


len(tweets)


# In[10]:


print(tweets[1])


# In[11]:


print(tweets[550])


# In[12]:


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# In[13]:


analyser = SentimentIntensityAnalyzer()


# In[14]:


for t in tweets:
    t["Sentiment"]=analyser.polarity_scores(t["Text"])


# In[15]:


type(tweets[0]["Sentiment"]["compound"])


# In[16]:


print(tweets[0]["Date"])


# In[17]:


import pymongo
import json


# In[18]:


c = pymongo.MongoClient("mongodb://localhost")


# In[19]:


db = c.kubrick


# In[20]:


collection = db.uberv2


# In[21]:


collection.insert(tweets)


# In[22]:


pipeline =[{"$group": {"_id": { "$dateToString": { "format": "%Y-%m-%d", "date": "$Date"}}, "average": {"$avg": "$Sentiment.compound"}}}]


# In[23]:


for result in collection.aggregate(pipeline):
    print(result)


# In[24]:


d={}

for result in collection.aggregate(pipeline):
    d[result["_id"]] = result["average"]


# In[25]:


d


# In[26]:


df = pd.DataFrame(data = d, index = [0])


# In[27]:


df


# In[28]:


df=df.T


# In[29]:


df


# In[30]:


get_ipython().magic('pylab inline')
plt.figure()


# In[31]:


df.plot(kind = 'line', legend=False)

