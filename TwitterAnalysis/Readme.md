===========================================
TWITTER Data Analysis using  Python
===========================================


### About The Data

Dats used is from Twitter website. Tweets are extracted for #Trump and #Hillary and compared 


### Dependencies
Make sure you have the following libraries installed before running the code.
-	argparse
-	requests
-	requests_oauthlib 
-	json
-	datetime 
-	TextBlob


 ### Usage 
twitter_analysis.py -h

- -s or -search searchterm
- -u or -until until date in the format YYYY-MM-DD
- -o or -output output json file name ex.. out.json


### Analysis Performed 
-	Estimating user reach by finding average number of friends of Trump Follower and Hillary followers for a time window 
-	For each topic, showing the top 10 retweeted tweets for every day during the time window.
-	Finding sentiment in Tweets. Analyzing overall sentiment of the day.
-	Identifying which states tweet more on the topic
-	Identifying influential tweets for each state 

