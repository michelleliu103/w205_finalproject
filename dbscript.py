import sys
import csv

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

#Create a Database
try:
        # CREATE DATABASE can't run inside a transaction
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute("CREATE DATABASE finalproject")
        cur.close()
        conn.close()

except:
        print "db is already created?"


#Connecting to tcount
conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

#Create a Table
try:
        cur = conn.cursor()
        # cur.execute("DROP TABLE IF EXISTS tweets;")
        cur.execute("CREATE TABLE tweets (id BIGSERIAL NOT NULL PRIMARY KEY, \
                tweet_id BIGINT NOT NULL, \
                tweet VARCHAR(250) NOT NULL, \
                user_handle VARCHAR(25), \
                mentions VARCHAR(250), \
                hashtags VARCHAR(250), \
                retweets INTEGER DEFAULT 0, \
                favorites INTEGER DEFAULT 0, \
                permalink VARCHAR(250), \
                japerk INTEGER DEFAULT 0, \
                textanalysis INTEGER DEFAULT 0, \
                sentimentapi INTEGER DEFAULT 0, \
                created_at TIMESTAMP NOT NULL, \
                inserted_at TIMESTAMP NOT NULL default now());")

        cur.execute("CREATE INDEX tweets_created_idx ON tweets (created_at);")
        cur.execute("CREATE INDEX tweets_tweet_idx ON tweets (tweet);")

except:
        print "Table is already created?"

if len(sys.argv)!=1:
        filename = sys.argv[1]
        print "Importing " + filename + "..."

        csv_data = csv.reader(file(filename), delimiter="\t")

        allofit = list(csv_data)

        # print "file length: " + str(len(allofit))


        for i in range(len(allofit)):
                try:
                        userhandle = allofit[i][0]
                        createdat = allofit[i][1]
                        retweets = allofit[i][2]
                        favorites = allofit[i][3]
                        tweets = allofit[i][4][:250].replace("'", "''")
                        mentions = allofit[i][6]
                        hashtags = allofit[i][7]
                        tweetid = allofit[i][8]
                        permalink = allofit[i][9][:250]

                        sql = "INSERT INTO tweets (user_handle, created_at, retweets, favorites, tweet, mentions, hashtags, tweet_id, permalink) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                        userhandle, createdat, retweets, favorites, tweets, mentions, hashtags, tweetid, permalink)

                        # print sql
                        cur.execute(sql)

                except:
                        print "nope."
                        print sys.exc_info()[0]
                        print "userhandle: " + userhandle
                        print "createdat: " + createdat
                        print "retweets: " + retweets
                        print "favorites: " + favorites
                        print "tweets: " + tweets
                        print "mentions: " + mentions
                        print "hashtags: " + hashtags
                        print "tweetid: " + tweetid
                        print "permalink: " + permalink
                        continue


cur.close()
conn.close()

                
