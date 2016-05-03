# -*- coding: utf-8 -*-
"""
Created on Mon May 02 13:46:36 2016

@author: Yudi Dong
"""
#Build a dictionary to store the scores of users.
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

##Create the list to store the user id in the test set
TEST_SET = 'RawData/testIdx2.txt'

user_id_test = []
with open(TEST_SET) as test_set:
    for line in test_set:
        if "|" in line:
            [user_id, number] = line.strip("\n").split("|")
            user_id_test.append(user_id)
            
##process the trackData2.txt : create a dictionary {"track_id":["album_id","artist_id"]}
TRACK_HI = "RawData/trackData2.txt"

lib_track ={}
with open(TRACK_HI) as track_hi:
    for line in track_hi:
        track_split=line.strip("\n").split("|")
        lib_track[track_split[0]] = [track_split[1], track_split[2]]

##create a dictionary to store the very test users' rating of tracks{"user_id":{"track_id":rating}}
TRACK_RATING = "Data/track_userrating.txt"

lib_user_trackRating ={}
nest_trackRating = {}
with open(TRACK_RATING) as track_rating:
    for line in track_rating:
        if "|" in line:
            [user_id, other] = line.strip("\n").split("|")
            nest_trackRating = {}
        else:
            [item_id,score] = line.strip("\n").split("\t")
            nest_trackRating[item_id] = score
            lib_user_trackRating[user_id] = nest_trackRating
            
##Create a dictionary {"user_id":{"track_id":[[album,artist],[albumtrack],[artisttrack]]} based on the test hierarchy
TEST_HI ="Data/test_hierarchy.txt"
LAST_SCORE = "Data/last_score.txt"


lib_test_hi = {} #{"user_id":{"track_id":[[album,artist],[albumtrack],[artisttrack]]}
index ={}
albumtrack = []
artisttrack = []
count = 0
with open(TEST_HI) as test_hi:
    for line in test_hi:
        if count == 6:
            count = 0
            index ={}
        count = count +1
        line_list = line.strip("\n").split("|")
        albumartist = [line_list[2],line_list[3]]
        for track_id in lib_user_trackRating[line_list[0]].keys():
            if lib_track[track_id][0] == line_list[2]:
                albumtrack.append(track_id)

            if lib_track[track_id][1] == line_list[3]:
                artisttrack.append(track_id)

        index[line_list[1]] = [albumartist,albumtrack,artisttrack]
        albumtrack = []
        artisttrack = []
        lib_test_hi[line_list[0]]=index


for user_id in user_id_test:
    for key in lib_test_hi[user_id]:
        if lib_userscore[user_id].has_key(lib_test_hi[user_id][key][0][0]):
            lib_test_hi[user_id][key][0][0] = lib_userscore[user_id][lib_test_hi[user_id][key][0][0]]
        else:
            lib_test_hi[user_id][key][0][0] = "None"
        if lib_userscore[user_id].has_key(lib_test_hi[user_id][key][0][1]):
            lib_test_hi[user_id][key][0][1] = lib_userscore[user_id][lib_test_hi[user_id][key][0][1]]
        else:
            lib_test_hi[user_id][key][0][1] = "None"
        if len(lib_test_hi[user_id][key][1]) !=0:
            for i in range(len(lib_test_hi[user_id][key][1])):
                if lib_userscore[user_id].has_key(lib_test_hi[user_id][key][1][i]):
                    lib_test_hi[user_id][key][1][i] = lib_userscore[user_id][lib_test_hi[user_id][key][1][i]]
                else:
                    lib_test_hi[user_id][key][1][i] = "None"
        if len(lib_test_hi[user_id][key][2]) !=0:
            for i in range(len(lib_test_hi[user_id][key][2])):
                if lib_userscore[user_id].has_key(lib_test_hi[user_id][key][2][i]):
                    lib_test_hi[user_id][key][2][i] = lib_userscore[user_id][lib_test_hi[user_id][key][2][i]]
                else:
                    lib_test_hi[user_id][key][2][i] = "None"

lib_lastScore = {}
for user_id in user_id_test:
    track_lastscore ={}
    for key in lib_test_hi[user_id]:
        score = 0
        if lib_test_hi[user_id][key][0][0] !="None":
            score = score + float(lib_test_hi[user_id][key][0][0])
        if lib_test_hi[user_id][key][0][1] !="None":
            score = score + float(lib_test_hi[user_id][key][0][1])*0.2
        if len(lib_test_hi[user_id][key][1]) !=0:
            for i in range(len(lib_test_hi[user_id][key][1])):
                if lib_test_hi[user_id][key][1][i] == "None":
                    lib_test_hi[user_id][key][1][i] = 0
                else:
                    lib_test_hi[user_id][key][1][i] = float(lib_test_hi[user_id][key][1][i])
            score = score + (sum(lib_test_hi[user_id][key][1])/len(lib_test_hi[user_id][key][1]))*0.1
        if len(lib_test_hi[user_id][key][2]) !=0:
            for i in range(len(lib_test_hi[user_id][key][2])):
                if lib_test_hi[user_id][key][2][i] == "None":
                    lib_test_hi[user_id][key][2][i] = 0
                else:
                    lib_test_hi[user_id][key][2][i] = float(lib_test_hi[user_id][key][2][i])
            score = score + (sum(lib_test_hi[user_id][key][2])/len(lib_test_hi[user_id][key][2]))*0.02
        track_lastscore[key] = score
    lib_lastScore[user_id] = track_lastscore

with open(LAST_SCORE,'w') as last_score:
    with open(TEST_HI) as test_hi:
        for line in test_hi:
            [user_id, track_id, other]=line.strip("\n").split("|",2)
            last_score.write(user_id+"|"+track_id+"|"+str(lib_lastScore[user_id][track_id])+"\n")
        
        

            
        
              
            
        
        