Steps to run the project
------------------------

1. set up the EC2 AMI with attached EBS volume as described in Exercise 2 instructions

2. create and connect to AMI following Lab 6 instructions

3. make sure these are installed on the instance (can use "pip install ..." as the root user)
        lxml==3.5.0
        pyquery==1.2.10

4. su - w205

5. configure and run getoldtweets.py
        a. edit getoldtweets.py in the w205_finalproject folder
        b. put in the desired "starttime" in the "YYYY-MM-DD" format
        c. Edit d1 and d2 to the desired start date and end date in date(YYYY,MM,DD) format

        The Python script will pull 1000 tweets per day, starting on the desired start date, every 7 days, until the desired end date.
        In our case, the start date was 2010-05-10 and our end date was 2017-03-01. The script will output the csv files for each day in the current directory.
        Each file has the headers: username; date; retweets; favorites; text; geo; mentions; hashtags; id; permalink

6. combine all the csv files for one given year into one file per year
        a. first put all the files in different folders by year
        b. within each folder, remove the header and then concatenate the files into one single file with the command:

        ls * | xargs -n 1 tail -n+2 > output_YYYY.csv
