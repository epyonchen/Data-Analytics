################################
### Creates Database
### Updates Database with Data
################################

import sqlite3 as lite
import sys
import os 
import csv
import urllib
import re

ratingsList = "http://boxnumbertwo.com/MovieData/ratings.list"
response = urllib.urlopen(ratingsList)
movies = dict()
votelist = list()
namelist = list()
count = 0
#count2 = 0 #  count numbers store in movies(dict)
for line in response: #  store names and ratings into movies(dict)
	words = re.sub(' +',' ',line.strip()) #  This is a string!
	save = words.split(" ",3) #  split vote, rating and name
	#print type(save[1])
	#print int(save[1].replace("'", ""))
	vote = int(save[1].replace("'", ""))
	#print vote
	votelist.append(vote) #  A list records all numbers of votes in order
	name = save[3].split(" (",1) #  Only part of  names have quotation, so we can not split name with quotation
	#print name
	namelist.append(name[0]) #  A list records all movies in order
	count = count +1
	print count
	count0 = 0
	while count0 < count: #  Find rate with the most vote in a same name
	     if (name[0] == namelist[count0] and vote > votelist[count0]): #  match current name with names in namelist, and compare the number of votes
	         movies[name[0]] = float(save[2].replace("'", ""))#  Store rate with the most vote in dict
	         #count2 = count2 +1
	     count0 = count0 + 1
#print movies
#print count2


## Set directory to computer
directoryForDB = "D:/Workshop/homework/Data Analytics/Lab3/"
if not os.path.exists(directoryForDB):
	os.makedirs(directoryForDB)

directoryForDB = directoryForDB + "movies.db"
## If database does not exist, creates items
## If database does exist, opens it
con = lite.connect(directoryForDB)
with con:
	ratings = con.cursor()
	ratings.execute("DROP TABLE IF EXISTS MoviesAndRatings") 
	ratings.execute("CREATE TABLE MoviesAndRatings(name TEXT, ratings REAL)")
	for key in movies:
	        insertStatement = """INSERT INTO MoviesAndRatings VALUES('%s',%f)""" % (key,movies[key]) #  Add movies' names and ratings into database
		ratings.execute(insertStatement)
	## NEEDED, if not, database does not update
	con.commit()
