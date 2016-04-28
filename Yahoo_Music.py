# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:17:16 2016

@author: Yudi Dong
"""
##############################################################################
'''
Phase1: GET THE TEST DATA HIERARCHY
'''
##############################################################################

TEST_DATA="RawData/testIdx2.txt"
TRACK_DATA = "RawData/trackData2.txt"
TEST_HIERARCHY = "Data/test_hierarchy.txt"

lib_trackData={}
with open(TRACK_DATA) as trackData:
	for line in trackData:
		# Build a dictionary: key is track id and value is track detail(artist,album,genre)
		[track_Id,track_detail] = line.strip("\n").split("|",1)
		lib_trackData[track_Id] = track_detail
  
# Load list of track items and save the hierarchy structure in a new file
with open(TEST_HIERARCHY,"w") as testHierarchy:
	# Open the source file, you can use your own source
	with open(TEST_DATA) as testData:
		for line in testData:
			# "|" represent user information
			if "|" in line:
				[cur_user,cur_track] = line.strip("\n").split("|")
			# Track item have no "|" in the line			
			else:
				cur_track = line.strip("\n")
				testHierarchy.write(cur_user+"|"+cur_track+"|"+lib_trackData[cur_track]+"\n")
    
  
##############################################################################
'''
Phase2: GET THE TEST SOCRE HIERARCHY
'''
##############################################################################

TEST_SCORE = 'Data/test_score.txt'
TEST_HIERARCHY = 'Data/test_hierarchy.txt'
USER_SCORE = 'RawData/trainIdx2.txt'       

#Build a dictionary to store the scores of users.
#Build a dictionary to store the scores of all items.
lib_userscore={}
lib_allscore = {}
with open(USER_SCORE) as userScore:
    for line in userScore:
        if "|" in line:
            [user_id,number] = line.strip("\n").split("|")
            lib_itemscore={}
        else:
            [item_id,score] = line.split()
            lib_itemscore[item_id]=score
            lib_allscore.setdefault(item_id,[]).append(score)#one item corresponds to all the ratings
            lib_userscore[user_id]=lib_itemscore
 
#one item corresponds to the mean of all the ratings
lib_meanscore = {}
for key in  lib_allscore:
    sum = 0
    for item in lib_allscore[key]:
        sum = sum + float(item)
    lib_meanscore[key] = sum / len(lib_allscore[key])

# Replace the items id with the scores of users.         
with open(TEST_SCORE,"w") as testScore:            
    with open(TEST_HIERARCHY) as testHie:
        for line in testHie:
            [user_id,track_id,items] = line.strip("\n").split("|",2)
            items_list = items.split("|")
            score =""
            count = 1
            for i in items_list:
                if lib_userscore[user_id].has_key(i):
                    i = lib_userscore[user_id][i]
                    score=score+"|"+i
                else:
                    i = '0'
                    score=score+"|"+i
            testScore.write(user_id+"|"+track_id+score+"\n")
            
##############################################################################
'''
Phase3: GET THE RECOMMENDATION RESULTS
'''
##############################################################################

RESULT = "Results/prediction.txt"		
TEST_SCORE = "Data/test_score.txt"

weight_five = [1,0.2,0.001,0.001,0.001]

# Caluate the sum of scores of very tracks
rating_list = []
with open(TEST_SCORE) as testScore:
    for line in testScore:
        [user_id, track_id, score]=line.strip("\n").split("|",2)
        score_list=score.split("|")
        rating = 0
        if len(score_list)>=len(weight_five):
            for i in range(len(weight_five)):
                rating = rating + float(score_list[i])*weight_five[i]
            rating_list.append(rating/len(weight_five))
        else:
            for i in range(len(score_list)):
                rating = rating + float(score_list[i])*weight_five[i]
            rating_list.append(rating/len(score_list))
        
                

#Sort the very 6 scores and label the three higest scores as "1" and label the three lowest scores as "0". 
#"1" means recommended and "0" means unrecommended
prediction = []
for i in range(len(rating_list)/6):
    segment = {}
    for j in range(6):
        segment[j]=rating_list[j+i*6]
    segment_sorted = sorted(segment.items(), key=lambda e:e[1], reverse=True)
    count = 0
    for item in segment_sorted:
        if count < 3:
            segment[item[0]] = 1       
        else:
            segment[item[0]] = 0
        count = count + 1
    for key in segment:
        prediction.append(segment[key])

with open(RESULT,'w') as result:
    for item in prediction:
        result.write(str(item)+'\n')
    



       


                    
                    
                

            
        