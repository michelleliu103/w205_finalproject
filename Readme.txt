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

7. combine all the csv files for one given year into one file per year
        a. first put all the files in different folders by year
        b. within each folder, remove the header and then concatenate the files into one single file with the command:

        ls *.csv | xargs -n 1 tail -n+2 > output_YYYY.csv

8. for each csv file of tweets, run the command "python dbscript.py filename.csv" to create a postgres database and populate it with the tweets

