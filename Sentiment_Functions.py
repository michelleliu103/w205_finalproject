import requests
import pandas as pd
import numpy as np
import json
import psycopg

def select_1000_tweets():
	conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()
	cur.execute("SELECT id, tweet from tweets where random() limit 1000")
	
	tweets = cur.fetchall()
	return tweets

def sentiment_analysis_api_1(tweet_list):
    """From text-processing.com"""
    for tweet in tweet_list:
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


def sentiment_analysis_api_2(tweet_list):
    """From sentimentanalysis.net"""    
    for tweet in tweet_list:
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

	
def sentiment_analysis_api_3(tweet_list):
    """From textualinsights.com"""
    for tweet in tweet_list:
        api_request = requests.post("https://sentimentapi.p.mashape.com/products/api/extractsentiment?", headers={
    "X-Mashape-Key": "",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  }, data={'text': tweet[1]})
        rating_dict = json.loads(api_request.text)
        rating = int(rating_dict["rating"])
            cur.execute("UPDATE tweets SET sentimentapi=%s WHERE id =%s", (rating,tweet[0]))


tweets = select_1000_tweets()

sentiment_analysis_api_1(tweets)
sentiment_analysis_api_2(tweets)
sentiment_analysis_api_3(tweets)

