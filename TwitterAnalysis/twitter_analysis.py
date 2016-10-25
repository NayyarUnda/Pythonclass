# Created on Wed Oct 19 17:57:03 2016
# author: nayyar unda

import os
import glob 
import textwrap
import argparse
import sys,getopt
import requests
from requests_oauthlib import OAuth1
import json
from datetime import datetime,date,timedelta
from textblob import TextBlob
from city_to_state import city_to_state_dict

def createPath(search,date):    
	if not os.path.exists('./'+search):
		print ('Creating folder..',search)		
		os.makedirs('./'+ search)
		
 
def searchAndSave(search, until, outFile): 

	# Variables that contains the user credentials to access Twitter API 
	ACCESS_TOKEN = '3225965314-MxyYm41OX5ubLf51Q9D37daddgPtckqkcQCqmsV'
	ACCESS_TOKEN_SECRET = 'etJJpyZixluagBJUL1EeDPSDgMMbH1E12LxbHjviRdj63'
	CONSUMER_KEY = 'XGEba7sz1k4KqkTX0g8VyNQJX'
	CONSUMER_SECRET = 'BZ6nHkEaQ4gIrWrsVAytV2L060p55P3EtlFcmIm6ExoMHGEwPs'
	url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
	auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	requests.get(url, auth=auth)
	
	# login complete
	print ('Searching tweets with keyword ',search,' and saving')
	search_url='https://api.twitter.com/1.1/search/tweets.json?&result_type=mixed&count=100'
	# add search term to the url
	search_string = '&q=%23' + search
	until= '&until=' + until
	search_url= search_url+ search_string + until	
	#print(search_url)
	r = requests.get(search_url, auth=auth)
	data = r.json()
	with open('./'+search+'/'+outFile, 'w') as f:
		json.dump(data, f)

def analysisAvgFriends(search,outFile):
	import time
	from collections import defaultdict
	friends={}
	path='./'+search+'/'	
	data = json.load(open(path+outFile))
	# count no of tweets downloaded
	no_of_tweets = len(data['statuses'])
	print("count no of tweets downloaded:",no_of_tweets)
	summary=open('./'+search+'/avgFriendsSummary.txt', 'w')
	
			
	for item in data['statuses']:
		temp_data=item['user']['created_at']
		date=time.strftime('%Y-%m-%d', time.strptime(temp_data,'%a %b %d %H:%M:%S +0000 %Y'))		
		friends_count= int(item['user']['friends_count'])
		#print("friends_count", friends_count)
		if (date in friends) == 0:
			friends[date]=[]			
		friends[date].append(friends_count)		
		
		
	for key in friends:
		#print(friends[key])
		avg_friends=0
		length = len(friends[key])
		if not os.path.exists('./'+search+'/'+key):
			print ('Creating folder..',key)		
			os.makedirs('./'+ search+'/'+key)	
		#print (key)
		for item in friends[key]:			
			if item !='-':
				avg_friends= avg_friends+ int(item)##########################################
			
		avg_friends=avg_friends/length
		#print('avg_friends: ', avg_friends)
		with open('./'+search+'/'+key+'/avgFriends'+key+'.txt', 'w') as f:##################################
			f.write('Avg no of friends for people whos tweets included the keyword: '+search+' on date: '+ str(key)+' are: '+ str(int(avg_friends)))
			summary.write('Avg no of friends for people whos tweets included the keyword: '+search+' on date: '+ str(key)+' are: '+ str(int(avg_friends))+'\n')
			f.close()	
	summary.close


def analysisTopTweets(search,outFile):
	import time
	from operator import itemgetter
	from collections import defaultdict
	retweets={}
	index = 0
	path='./'+search+'/'	
	data = json.load(open(path+outFile))
	# count no of tweets downloaded			
	for item in data['statuses']:
		temp_data=item['created_at']
		date=time.strftime('%Y-%m-%d', time.strptime(temp_data,'%a %b %d %H:%M:%S +0000 %Y'))		
		retweet_count= int(item['retweet_count'])
		retweet_text=item['text']		
		
		if (date in retweets) == 0:
			retweets[date]={}
		if (retweet_count in retweets[date]) == 0:	
			retweets[date][retweet_count]=[]
			
		retweets[date][retweet_count].append(retweet_text)
		#retweets[date].append(retweet_count)		
	new_list=[]
	tweets_list=[]				
	for date in retweets:
		if not os.path.exists(path+date):
			print ('Creating folder..',date)		
			os.makedirs(path+date)
		fout=open(path+date+'/top10.txt','w') 			
		for count in retweets[date]:	
			new_list.append(count)
		
		new_list.sort(reverse=True)
		track = 0
		for item in new_list:
			track = track + 1
			if track <= 10:				
				fout.write("count: "+str(item)+' ' )
				tweets_list=retweets[date][item]
				for tweet in tweets_list:						
					temp= tweet.encode('utf8')
					fout.write(str(temp)+'\n')
			else: break	
		new_list=[]
		tweets_list=[]	
		fout.close()

def sentimentalanalysis	(search,outFile):
	import time
	sentiment={}
	path='./'+search+'/'	
	data = json.load(open(path+outFile))
	for item in data['statuses']:
		temp_data=item['created_at']
		date=time.strftime('%Y-%m-%d', time.strptime(temp_data,'%a %b %d %H:%M:%S +0000 %Y'))
		tweet = str(item['text'].encode('utf8'))
		if (date in sentiment) == 0:
			sentiment[date]=[]			
		sentiment[date].append(tweet)
		print(date)
	neg=0
	pos=0
	neut=0
	for date in sentiment:
		if not os.path.exists(path+date):
			print ('Creating folder..',date)		
			os.makedirs(path+date)
		fout=open(path+date+'/sentiments.txt','w')
		print("sentiment analysis",date)
		for key in sentiment[date]:
			text=TextBlob(key)
			if text.sentiment.polarity < 0:
				sent = "negative"
				neg=neg +1
			elif text.sentiment.polarity == 0:
				sent = "neutral"
				neut=neut +1
			else:
				sent = "positive"
				pos= pos +1
			temp=sent + str(key)
			temp= temp.encode('utf8')
			fout.write(str(temp)+'\n')	
		print ("negative sentiments",neg)
		print ("positive sentiments",pos)
		print("nuetral sentiments",neut)
		
		fout.close()
		
		
def stateAnalysis(search,outFile):	
	location={}
	import re
	path='./'+search+'/'	
	data = json.load(open(path+outFile))
	state_count={}
	for item in data['statuses']:
		parts=re.split(',| |!',item['user']['location'])
		#print(parts)
		for item in parts:
			if item !='' and item != ',' and item !='!':
				if (item in city_to_state_dict):	
					state= city_to_state_dict[item]				
					if (state in location) == 0:
						location[state]=[]					
						location[state] = 1
					else:
						location[state] = location[state]+ 1	
					break
		
	for item in location:
		print(item+': no of tweets=')
		print(str(location[item]))

def influntialTweetsState(search,outFile):
	location={}
	import re
	path='./'+search+'/'	
	data = json.load(open(path+outFile))
	state_count={}
	for item in data['statuses']:
		retweet_text=item['text']
		retweet_count= int(item['retweet_count'])
		followers_count=int(item['user']['followers_count'])
		count=followers_count * retweet_count
		
		parts=re.split(',| |!',item['user']['location'])
		#print(parts)
		for item in parts:
			if item !='' and item != ',' and item !='!' and count !=0:
				if (item in city_to_state_dict):	
					state= city_to_state_dict[item]
					if (state in location) == 0:
						location[state] = {}
					if (count in location[state])== 0:
						location[state][count]=[]
									
					location[state][count].append(retweet_text)	
					
				
					
	new_list=[]
	tweets_list=[]				
	for state in location:
		if not os.path.exists(path+state):
			print ('Creating folder..',state)		
			os.makedirs(path+state)
		fout=open(path+state+'/topInfluentialTweets.txt','w') 
		
		for count in location[state]:	
			new_list.append(count)
			#print(count)
			
		new_list.sort(reverse=True)
		
		for item in new_list:
			fout.write("count: "+str(item)+' ' )			
			tweets_list=location[state][item]
			for tweet in tweets_list:			
				temp= tweet.encode('utf8')
				fout.write(str(temp)+'\n')
				#print(temp)
		new_list=[]
		tweets_list=[]	
		fout.close()		
					

		
	


def main(argv):
	parser = argparse.ArgumentParser(
	prog='twitter_search.py',
	formatter_class=argparse.RawDescriptionHelpFormatter,
	description=textwrap.dedent('''\
	Valid Input Required
	-----------------------------------------------------
	-s or -search searchterm
	-u or -until until date in the format YYYY-MM-DD 
	-d or -date date in the format YYYY-MM-DD 
	-o or -output output json file name ex.. out.json	
	'''))
	parser.add_argument('-search','-s', default='trump')
	parser.add_argument('-until','-u', default='2016-10-20')
	parser.add_argument('-out','-o', default='out.json')
	parser.add_argument('-date','-d', default='2016-10-20')

	args = parser.parse_args()

	print ('Starting...')
	print ('Search term:', args.search)
	print ('Output file:', args.out)
	createPath(args.search,args.date)	
	searchAndSave(args.search, args.until, args.out)
	print ("Your options are :")
	print ("1)For a given search term and a time window, what is the average number of friends a user has each day.")
	print ("2)For each topic, show the top 10  retweeted tweets for every day during the time window.")
	print ("3)Sentimental Analysis")
	print ("4)state wise tweet analysis ")
	print ("5)Top influential tweet for each state.")
	
	
	choice=int(input("Choose your analysis : "))
	
	if choice == 1:
		print("I m here ")
		analysisAvgFriends(args.search,args.out)
	elif choice == 2:
		analysisTopTweets(args.search,args.out)
	elif choice == 3:
		sentimentalanalysis(args.search,args.out)
	elif choice == 4:
		stateAnalysis(args.search,args.out)
	elif choice == 5:
		influntialTweetsState(args.search,args.out)
	
	#analysisAvgFriends(args.search,args.out)	
	#analysisTopTweets(args.search,args.out)
	#sentimentalanalysis(args.search,args.out)
	#stateAnalysis(args.search,args.out)
	#influntialTweetsState(args.search,args.out)
	print("End")	
	
	
if __name__=='__main__':	
	main(sys.argv[1:])




