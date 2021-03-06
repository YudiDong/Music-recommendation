# -*- coding: utf-8 -*-
"""
Created on Mon May 02 23:47:50 2016

@author: Yudi Dong
"""
##Calculate the mean score of genres
TEST_HIERARCHY = 'Data/test_hierarchy.txt'
USER_SCORE = 'RawData/trainIdx2.txt'       

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
            lib_userscore[user_id]=lib_itemscore   
genreScore =[] 
              
with open(TEST_HIERARCHY) as testHie:
    for line in testHie:
        index = []
        [user_id,track_id,items] = line.strip("\n").split("|",2)
        items_list = items.split("|")
        for i in range(2,len(items_list)):
            if lib_userscore[user_id].has_key(items_list[i]):
                a = lib_userscore[user_id][items_list[i]]
                index.append(float(a))
        genreScore.append(index)

last_genrescore=[]
for item in genreScore:
    if len(item) !=0:
        last_genrescore.append((sum(item)/len(item))*0.01)
    else:
        last_genrescore.append(0.0)



##album rating, artist rating, mean of tracks ratings in album, mean of tracks ratings in artist, mean of genre ratings. 
##These four ratings are decided whether we recommend the track. Moreover, we also set the weight of four ratings[1,0.2,0.1,0.02,0.01]
LAST_SCORE = "Data/last_score.txt"
RESULT = "Results/prediction.txt"		

rating_list = []
count = 0
with open(LAST_SCORE) as last_score:
    for line in last_score:
        [user_id, track_id, score]=line.strip("\n").split("|")
        rating_list.append(float(score)+last_genrescore[count])
        count=count+1

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
        
            