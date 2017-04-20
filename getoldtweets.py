import got
import codecs
from datetime import date, timedelta


search_term = 'obamacare%20OR%20aca'

starttime = '2009-01-01'
#starttime = '2010-05-10'
#starttime = '2011-07-02'
#starttime = '2013-10-19'

#start date
#d1 = date(2009,1,1)
d1 = date(2010, 5, 10) 
#d1 = date(2011, 1, 24)
#d1 = date(2011, 7, 2)
#d1 = date(2016, 01, 01)
d2 = date(2016, 12, 31)  # end date

list=[starttime]

current = d1
while current < d2:
        current += timedelta(days=7)
        #print current
        list.append(str(current))


def receiveBuffer(tweets):
        for t in tweets:
                # outputFile.write(('\n%s;%s;%d;%d;"%s";%s;%s;%s;"%s";%s' \
                outputFile.write(('\n%s\t%s\t%d\t%d\t"%s"\t%s\t%s\t%s\t"%s"\t%s' \
                % (t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, \
                t.favorites, t.text, t.geo, t.mentions, t.hashtags, t.id, t.permalink)))
        outputFile.flush();

        print '%d more saved to file...\n' % len(tweets)

for start_time in list:
        end_time = start_time[0:8] + str(int(start_time[-2:])+1)
        print 'start time is %s, end time is %s\n' % (start_time, end_time)
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(search_term).setSince(start_time).setUntil(end_time).setMaxTweets(1000)
        filename = "output_date" + start_time + ".csv"
        outputFile = codecs.open(filename, "w+", "utf-8")
        outputFile.write('username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink')
        got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)
        outputFile.close()

