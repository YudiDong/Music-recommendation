# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 15:40:21 2016

@author: Yudi Dong
"""

## CREATE THE TEST DATA HIERARCHY AND STORE AS test_hierarchy.txt

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
