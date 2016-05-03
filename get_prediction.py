# -*- coding: utf-8 -*-
"""
Created on Mon May 02 23:47:50 2016

@author: Yudi Dong
"""

##
LAST_SCORE = "Data/last_score.txt"
RESULT = "Results/prediction.txt"		

rating_list = []
with open(LAST_SCORE) as last_score:
    for line in last_score:
        [user_id, track_id, score]=line.strip("\n").split("|")
        rating_list.append(float(score))

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
        
            