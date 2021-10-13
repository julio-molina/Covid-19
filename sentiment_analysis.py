import pandas as pd
import numpy as np
import json
import csv
import re 
from textblob import TextBlob
from langdetect import detect
positive_count=0
neutral_count=0
negative_count=0
with open('tweepy_output.txt','r') as fp:
    reader = csv.reader(fp)
    next(reader)
    jsons = [row[2].split(",") for row in reader]
    
t=str(jsons[1])
total_count=0
for i in range(len(jsons)):
    try:
        t=str(jsons[i])
        x=t.split('full_text')
        xt=str(x[1])
        y=xt.split(',')
        full_text=y[0]
        clean_text=re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", full_text)
        analysis=TextBlob(clean_text)
        print(analysis)
        print(analysis.sentiment.polarity)
        total_count=total_count+1
        if analysis.sentiment.polarity > 0: 
            print('positive')
            positive_count=positive_count+1
        elif analysis.sentiment.polarity == 0: 
            print ('neutral')
            neutral_count=neutral_count+1
        else: 
            print ('negative')
            negative_count=negative_count+1
    except:
        print("Error")

pos_percent=positive_count/total_count
neg_percent=negative_count/total_count
Neutral_percent=neutral_count/total_count
print('Results')
print('Positive Percentage={:0.2f}, Negative Percentage={:0.2f}, Neutral Percentage={:0.2f}'.format(pos_percent, neg_percent, Neutral_percent))

    
