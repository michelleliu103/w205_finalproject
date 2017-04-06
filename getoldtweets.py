import got
import codecs
from datetime import date, timedelta

search_term = 'obamacare%20OR%20afa'

#starttime = '2010-05-10'
#starttime = '2011-01-24'
starttime = '2012-07-23'

#d1 = date(2010, 5, 10)  # start date
#d1 = date(2011, 1, 24)
d1 = date(2012, 7, 23)
d2 = date(2017, 3, 1)  # end date

list=[starttime]

current = d1
while current < d2:
	current += timedelta(days=7)
	#print current
	list.append(str(current))


def receiveBuffer(tweets):
        for t in tweets:
                outputFile.write(('\n%s;%s;%d;%d;"%s";%s;%s;%s;"%s";%s' \
                % (t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, \
                t.favorites, t.text, t.geo, t.mentions, t.hashtags, t.id, t.permalink)))
        outputFile.flush();
        print 'More %d saved on file...\n' % len(tweets)

for start_time in list:
	end_time = start_time[0:8] + str(int(start_time[-2:])+1)
	print 'start time is %s, end time is %s\n' % (start_time, end_time)
	tweetCriteria = got.manager.TweetCriteria().setQuerySearch(search_term).setSince(start_time).setUntil(end_time).setMaxTweets(1000)
	filename = "output_date" + start_time + ".csv"
	outputFile = codecs.open(filename, "w+", "utf-8")
	outputFile.write('username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink')
	got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)
	outputFile.close()

#tweetCriteria = got.manager.TweetCriteria().setQuerySearch(search_term).setSince("2016-01-01").setUntil("2016-01-07").setMaxTweets(5000)
#tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
#got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)


#outputFile = codecs.open("output_got.csv", "w+", "utf-8")
#outputFile.write('username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink')

#def receiveBuffer(tweets):
#	for t in tweets:
#		outputFile.write(('\n%s;%s;%d;%d;"%s";%s;%s;%s;"%s";%s' \
#	 	% (t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, \
#	 	t.favorites, t.text, t.geo, t.mentions, t.hashtags, t.id, t.permalink)))
#	outputFile.flush();
#	print 'More %d saved on file...\n' % len(tweets)


#got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)
#outputFile.close()
#print tweet.text.encode('utf-8')
