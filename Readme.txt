Steps to run the project
------------------------

1. set up the EC2 AMI with attached EBS volume as described in Exercise 2 instructions
        if "df -k" doesn't show a /data volume...
                use "fdisk -l" to find path and 
                "mount -t ext4 (path) /data" to mount it

2. Start postgres with "/data/start_postgres.sh"

3. make sure these are installed on the instance (can use "pip install ..." as the root user)
        lxml==3.5.0
        pyquery==1.2.10

4. su - w205

5. "git clone https://github.com/michelleliu103/w205_finalproject.git" to download these files.

6. configure and run getoldtweets.py
        a. edit getoldtweets.py in the w205_finalproject folder
        b. put in the desired "starttime" in the "YYYY-MM-DD" format
        c. Edit d1 and d2 to the desired start date and end date in date(YYYY,MM,DD) format

        The Python script will pull 1000 tweets per day, starting on the desired start date, every 7 days, until the desired end date.
        In our case, the start date was 2009-01-01 and our end date was 2017-04-15. The script will output the csv files for each day in the current directory.
        Each file has the headers: username; date; retweets; favorites; text; geo; mentions; hashtags; id; permalink
        Note. The error "Twitter weird response" would come up if it fails to get a JSON response from the URL. Re-run the code will if this error appears.

7. remove the header and then concatenate the files into one single file with the command:

        ls *.csv | xargs -n 1 tail -n+2 > output.csv

8. run the command "python dbscript.py output.csv" to create a postgres database and populate it with the tweets

9. Run the command "python Sentiment_Functions.py" to take a sampling of
tweets from the database, call two sentiment analysis APIs to determine the sentiment
of the tweets, and update the database with the sentiment results. To change
the number of tweets sampled, modify the argument passed into the
sample_tweets function (at the bottom of the script). Note - the
API keys have been omitted from the code. Please reach out to jamaralex on
Slack or email jamaralex@gmail.com for the keys. If you are running the script
with python 2, you may see warnings related to upgrading to a newer
version. You can safely ignore these.  

10. To take a quick look and confirm the tweets and sentiment scores are successfully stored:
        a. start postgres $ psql -U postgres
        b. log into the database: \c finalprojecttweets
        c. look at the tables in the database: \d
        
11. To connect postgres database to Tableau:
        a. set up the ODBC PostgresSQL connection with databasename, server, port, username and password created in step 8. Test connection to make sure it successully connected.
        b. Connect Tableau Desktop with "To a Server"-> PostgresSQL -> and fill in all info used in previous steps
        
12. Go to KPP's website to download the lastest poll result data:
        a. Go to: http://kff.org/interactive/kaiser-health-tracking-poll-the-publics-views-on-the-aca/#?response=Favorable--Unfavorable--Don't%2520Know
        b. Share/Download -> Download Data
        c. Reverse pivot the data and imported to Tableau
        
13. To refresh Tableau dashboard in the future: 
        a. do step 12 a,b
        b. open Tableau and refresh and save (re-extract both data is recommended because this will speed up the dashboard when used)
        c. save (or if you have a Tableau server, you can publish it)

