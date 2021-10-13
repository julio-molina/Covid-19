import tweepy
import pandas as pd
import numpy as np
import json
from langdetect import detect
consumer_key=None
consumer_secret=None
access_token=None
access_token_secret=None
consumer_key='0PZdJ1dTtdgntTJeVdFT0sK28'
consumer_secret='U9IIRpok4pkzPrfFoq3mtbZvEXVkxDvC2uK7gZ79zdyPbYDsiR'
access_token='1313511693134319620-IBCssprtS9DmYRrevIvY08rJNthQBq'
access_token_secret='4Bh3Glu3VJADpQII95hPzlbRtfXyHhwfxnuCf4O3EtpsO'
if consumer_key == None:
  print("Error!: No key's Present")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
i=0
j=0
julio=0
file0 = open('tweepy_output.txt','a')
file0.write('location,id,json\n')
file0.close

with open('coronavirus.txt', 'r') as fp:
    while True:
        try:
            julio=julio+1
            example=fp.readline()
            exampleStr = api.get_status(example,tweet_mode="extended")
            p=exampleStr.full_text
            lang= detect(p)
            line = fp.readline()
            cnt = 1
            t=exampleStr._json
            line = fp.readline()
            cnt += 1   
            if (lang == 'en'):
                print("\n")
                if (t['user']['location']==''):#['user']['location']==''):
                    print("Nothing")
                else:
                    file0 = open('blank10.txt','a')
                    print("test good, write and seperate\n")

                    example=example.strip('\n')
                    example=example.strip('\t')
                    file0.write('"'+t['user']['location']+'"'+','+'"'+example+'"'+','+'"'+str(t)+'"')
                    file0.write('\n')
                    file0.close()

        except:
            print("Error\n")
            pass
file0.close()
