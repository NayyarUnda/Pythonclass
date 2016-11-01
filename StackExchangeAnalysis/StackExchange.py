



import requests
from requests_oauthlib import OAuth1
import json
import os 
import re 





def saveQuestions():
	for number in range (1,100):
		PageNo=str(number)
		print(number)
		url='https://api.stackexchange.com/2.2/questions?page=%s&pagesize=100&order=desc&sort=activity&tagged=pandas;python&site=stackoverflow&key=iN)OEQlB1cMs1zNLgT4piQ((&/'%number
		print(url)
		data= requests.get(url)
		data =data.text	
		pandasPython=json.loads(data)
		print(data.encode('utf'))
		fp=open('./Questions/'+PageNo+'_pandasPython.json','w')
		fp.write(json.dumps(pandasPython))
		fp.close()	




def saveUsers():
	for number in range (1,100):
		PageNo=str(number)
		print(number)
		url='https://api.stackexchange.com/2.2/users?page=%s&pagesize=100&order=desc&sort=reputation&site=stackoverflow&filter=!9YdnSASUf&key=iN)OEQlB1cMs1zNLgT4piQ((&/'%number
		print(url)
		data= requests.get(url)
		data =data.text	
		user=json.loads(data)
		print(data.encode('utf'))
		fp=open('./Users/'+PageNo+'_user.json','w')
		fp.write(json.dumps(user))
		fp.close()	

def saveQuestionTags():
	for number in range (1,100):
		PageNo=str(number)
		print(number)
		url='https://api.stackexchange.com/2.2/questions?page=%s&pagesize=100&order=desc&sort=activity&site=stackoverflow&filter=!9YdnSHzjM&key=iN)OEQlB1cMs1zNLgT4piQ((&/'%number
		print(url)
		data= requests.get(url)
		data =data.text	
		user=json.loads(data)
		print(data.encode('utf'))
		fp=open('./QuestionTags/'+PageNo+'_questionTag.json','w')
		fp.write(json.dumps(user))
		fp.close()	
	
def userTagAnalysis():
	i=0
	User={}
	tagUser={}
	path_to_json = 'Users/'
	for item in os.listdir(path_to_json):
		print(item)
		
		if item.endswith('.json'):
			file = item     
			file = "./Users/" + file
			P = json.load(open(file))
			for index in P['items']:
				userid=index['user_id']
				userName=index['display_name']
				userlink=index['link']
				reputation=index['reputation']
				url2='https://api.stackexchange.com/2.2/users/%s/tags?order=desc&sort=popular&site=stackoverflow&key=iN)OEQlB1cMs1zNLgT4piQ((&'%userid
				userTag=requests.get(url2)
				userTag=userTag.text
				tags=json.loads(userTag)
				if 'items' in tags:
					
					#print(tags)
					#print('-----------------------------------------------')
					#print(index) 
					for key in tags['items']:
						
						#print(key) 
						tag=key['name']	
						
						userProfile=(str(userid) + '  ' +userName +'  ' +userlink )
						if(tag not in tagUser) :
							tagUser[tag]={}	
						if(userid not in tagUser[tag]) :			
							tagUser[tag][reputation]={}						
						tagUser[tag][reputation]=userProfile

	
	#print(tagUser)
	for item in tagUser:
		fp=open('./UserTagAnalysis/'+item,'w')
		newlist= []
		for element in tagUser[item]:
				#print(element)
				newlist.append(int(element))
		newlist.sort(reverse=True)
		top = newlist[0]	
		print( item,tagUser[item][top])
		fp.write(str(tagUser[item]))
		fp.close()

	


def topQuestions():
	i=0
	questions={}
	path_to_json = 'Questions/'
	for item in os.listdir(path_to_json):
		if item.endswith('.json'):
			file = item     
			file = "./Questions/" + file
			P = json.load(open(file))
			for index in P['items']:
				if i== 20 :
					break
				i=i+1
				question = index['title']
				userid=str(index['owner']['user_id'])
				url2='https://api.stackexchange.com/2.2/users/'+userid+'?order=desc&sort=reputation&site=stackoverflow&key=iN)OEQlB1cMs1zNLgT4piQ((&'
				userProfile=requests.get(url2)
				userProfile=userProfile.text
				badges=json.loads(userProfile)
			for items in badges['items'] :
				temp= items['badge_counts']['bronze']+items['badge_counts']['silver']+items['badge_counts']['gold']
				questions[question]=temp

	temp_list=[]
	temp_list=sorted(questions, key=questions.__getitem__,reverse=True)
	for item in temp_list:
		print (item)
		print(questions[item])

	

def popularBadges():
	badge_types={}
	i=0
	j=0
	path_to_json = 'Questions/'
	for item in os.listdir(path_to_json):
		if item.endswith('.json'):
			file = item     
			file = "./Questions/" + file
			P = json.load(open(file))
			for index in P['items']:
				if i== 20 :
					break
				i=i+1
				userid=index['owner']['user_id']
				url2='https://api.stackexchange.com/2.2/users/%s/badges?order=desc&sort=rank&site=stackoverflow&key=iN)OEQlB1cMs1zNLgT4piQ(('%userid
				userbadge=requests.get(url2)
				userbadge=userbadge.text
				user_badges=json.loads(userbadge)
				for items in user_badges['items'] :
					badge_name= items['name']
					if (badge_name in badge_types) == 0:
						badge_types[badge_name]=[]
						badge_types[badge_name]=1
					else:
						badge_types[badge_name]=badge_types[badge_name]+1
		    
	temp_list=[]	
	temp_list=sorted(badge_types, key=badge_types.__getitem__,reverse=True)
	print("top 10 popular badges with their counts :")
	for item in temp_list:
		if j== 20 :
			break
		j=j+1
		print (item)
		print(badge_types[item])

		
def  tagAnalysis():
	i=0
	j=0
	questions={}
	answers_count={}
	path_to_json = 'QuestionTags/'
	for item in os.listdir(path_to_json):
		if item.endswith('.json'):
			file = item     
			file = "./QuestionTags/" + file
			P = json.load(open(file))
			
			for index in P['items']:
				
				answer_count=index['answer_count']
				
				#print (index['tags'])
				for key in index['tags']:
					#print(key)
					tag = key
					if (tag in questions) == 0:
						questions[tag]=1		
					else:
						questions[tag]= questions[tag] + 1
					if (tag in answers_count) == 0:
						answers_count[tag]=0
					else:
						answers_count[tag]= answers_count[tag] + answer_count
																
						
	
	
	temp_list1=[]	
	temp_list1=sorted(questions, key=questions.__getitem__,reverse=True)
	
	for item in temp_list1:
		if i==10:
			break
		i=i+1
		print ("tags",item,"tags_count",questions[item])
		
		
	temp_list2=[]	
	temp_list2=sorted(answers_count, key=answers_count.__getitem__,reverse=True)

	for item in temp_list2:
		if j==10:
			break
		j=j+1
		print ("tags",item,"answer_count",questions[item])
	
					
				

	




def userDownvoted():
	i=0
	User={}
	path_to_json = 'Users/'
	for item in os.listdir(path_to_json):
		if item.endswith('.json'):
			file = item     
			file = "./Users/" + file
			P = json.load(open(file))
			for index in P['items']:
				downvoteCount = index['down_vote_count']
				userid=index['user_id']
				User[userid]=downvoteCount

	temp_list=[]
	temp_list=sorted(User, key=User.__getitem__,reverse=True)
	for item in temp_list:
		if i== 1 :
			break
		i=i+1
		print ("user id ",item)
		print("Downvote count",User[item])


	
print("start")
saveQuestions()     
saveUsers()
saveQuestionTags()

print ("Welccome Your options are :")
print ("1)Show top questions according to the weightage.")
print ("2)Find reputed users for every topic ")
print ("3)What are Popular badges among users ")
print ("4)For each tag, calculate number of question asked and how many times it has been answered")
print ("5)User with most downvoted questions.")

choice=int(input("Choose your analysis : "))

if choice == 1:
	topQuestions()
	
elif choice == 2:
	userTagAnalysis()
elif choice == 3:
	popularBadges()
elif choice == 4:
	tagAnalysis()
elif choice == 5:
	userDownvoted()


print("End")	

	

	
	
	 

