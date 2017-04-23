import requests
import pandas as pd
import numpy as np
import json
import psycopg2

def sample_tweets():
    conn = psycopg2.connect(database="finalprojecttweets", user="postgres", password="pass", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT id, tweet from tweets order by random() limit 10")
	
    tweets = cur.fetchall()
    return tweets

def sentiment_analysis_api_1(tweet_list):
    """From text-processing.com"""
    conn = psycopg2.connect(database="finalprojecttweets", user="postgres", password="pass", host="localhost", port="5432")
    cur = conn.cursor()
    count = 0
    for tweet in tweet_list:
	print("API Request #: " + str(count))
	count += 1
        api_request = requests.post("https://japerk-text-processing.p.mashape.com/sentiment/", headers={
    "X-Mashape-Key": "",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  }, data={'text': tweet[1]})
        rating_dict = json.loads(api_request.text)
        rating = rating_dict["label"]
        if rating == "neutral":
            cur.execute("UPDATE tweets SET japerk=0 WHERE id =%s", (tweet[0],))
        elif rating == "pos":
            cur.execute("UPDATE tweets SET japerk=1 WHERE id =%s", (tweet[0],))
        elif rating == "neg":
            cur.execute("UPDATE tweets SET japerk=-1 WHERE id =%s", (tweet[0],))
    conn.commit()
    conn.close()

def sentiment_analysis_api_2(tweet_list):
    """From sentimentanalysis.net"""    
    conn = psycopg2.connect(database="finalprojecttweets", user="postgres", password="pass", host="localhost", port="5432")
    cur = conn.cursor()
    count = 0
    for tweet in tweet_list:
	print("API Request #: " + str(count))
	count += 1
        api_request = requests.post("https://textanalysis-text-sentiment-v1.p.mashape.com/sentiment-analyzer", headers={
    "X-Mashape-Key": "",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  }, data={'text': tweet[1]})
        rating_dict = json.loads(api_request.text)
        rating = rating_dict["sentiment"]
        if rating == "neutral":
            cur.execute("UPDATE tweets SET textanalysis=0 WHERE id =%s", (tweet[0],))
        elif rating == "positive":
            cur.execute("UPDATE tweets SET textanalysis=1 WHERE id =%s", (tweet[0],))
        elif rating == "negative":
            cur.execute("UPDATE tweets SET textanalysis=-1 WHERE id =%s", (tweet[0],))
    conn.commit()
    conn.close()


tweets = sample_tweets()

sentiment_analysis_api_1(tweets)
sentiment_analysis_api_2(tweets)

