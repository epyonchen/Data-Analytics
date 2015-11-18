import sqlite3 as lite
import sys
import os 

con = None
directoryForDB = "D:/Workshop/homework/Data Analytics/Lab 7/"
if not os.path.exists(directoryForDB):# If database does not exist, creates items
	os.makedirs(directoryForDB)	
directoryForDB = directoryForDB + "twitter.db"
con = lite.connect(directoryForDB)

with con:# Create database
	pop = con.cursor()
	pop.execute("DROP TABLE IF EXISTS node") 
	pop.execute("CREATE TABLE node(nodeid TEXT, time TEXT,PRIMARY KEY(nodeid))")# Set nodeid as Primary key to avoid dupicate
	pop.execute("DROP TABLE IF EXISTS link") 
	pop.execute("CREATE TABLE link(nodeid TEXT, linkto TEXT, time TEXT, PRIMARY KEY(nodeid, linkto))")# Set nodeid, linkto as Primary key, one link appears only once
	con.commit()
