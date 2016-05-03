# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:12:26 2016

@author: Yudi Dong
"""
##Create the list to store the user id in the test set
TEST_SET = 'RawData/testIdx2.txt'

user_id_test = []
with open(TEST_SET) as test_set:
    for line in test_set:
        if "|" in line:
            [user_id, number] = line.strip("\n").split("|")
            user_id_test.append(user_id)
        

##Create track_userrating.txt which contains the test set users's rating of very tracks.
USER_RATING = 'RawData/trainIdx2.txt'
ALBUM_ID = 'RawData/albumData2.txt'
ARTIST_ID = 'RawData/artistData2.txt'
GENRE_ID = 'RawData/genreData2.txt'
TRACK_RATING = "Data/track_userrating.txt"

non_track_idlist = []
with open(ALBUM_ID) as album:
    for line in album:
        albumlist= line.strip("\n").split("|")
        non_track_idlist.append(albumlist[0])
        
with open(ARTIST_ID) as artist:
    for line in artist:
        artistlist = line.strip("\n")
        non_track_idlist.append(artistlist)

with open(GENRE_ID) as genre:
    for line in genre:
        genrelist = line.strip("\n")
        non_track_idlist.append(genrelist)
        
with open(TRACK_RATING,'w') as track_userrating:
    with open(USER_RATING) as user_rating:
        for line in user_rating:
            if "|" in line:
                [user_id, number] = line.strip("\n").split("|")
                if user_id in user_id_test:
                    track_userrating.write(user_id+"|"+"Track"+"\n")
            else:
                [item_id,score] = line.strip("\n").split("\t")
                if user_id in user_id_test:
                    if item_id not in non_track_idlist:
                        track_userrating.write(item_id+"\t"+score+"\n")
                
'''
lib_user_trackRating ={}
nest_trackRating = {}
with open(USER_RATING) as user_rating:
    for line in user_rating:
        if "|" in line:
            [user_id, number] = line.strip("\n").split("|")
            nest_trackRating = {}
        else:
            [item_id,score] = line.strip("\n").split("\t")
            nest_trackRating[item_id] = score
            lib_user_trackRating[user_id] = nest_trackRating
'''


