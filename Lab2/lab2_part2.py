################################
### Connects to Database
### Gets Data from Database
################################

import sqlite3 as lite
import sys
import os 

con = None

## Creates a folder for the database
## Set directory to YOUR computer and folder
directoryForDB = "D:/Workshop/homework/Data Analytics/Lab2/" + "pittsburghData.db"

con = lite.connect(directoryForDB)
##########################################
#### Output: Neighborhood, (pop2010 - pop1940) as difference: ORDER by difference DESC
##########################################
with con:
	cur = con.cursor()    
	cur.execute("SELECT neighborhood, pop2010 - pop1940 FROM popANDdensity ORDER BY neighborhood DESC")
	rows = cur.fetchall()
	print "Output: Neighborhood, (pop2010 - pop1940) as difference: ORDER by difference DESC"
	for row in rows:
		print row[0],row[1]

##########################################
#### Output: Neighborhood, pop2010, Information
##########################################
with con:
	cur = con.cursor()
	cur.execute("SELECT p.neighborhood, p.pop2010, e.jobInformation FROM popANDdensity p, employment e WHERE p.neighborhood = e.neighborhood")
	rows = cur.fetchall()
	print "\nOutput: Neighborhood, pop2010, Information"
	for row in rows:
		print row[0],row[1],row[2]	
		
##########################################
#### Output: Neighborhood, MAX(pop2010)
##########################################
with con:
	cur = con.cursor()    
	cur.execute("SELECT neighborhood, MAX(pop2010) FROM popANDdensity WHERE pop2010=(SELECT MAX(pop2010)FROM popANDdensity)")
	rows = cur.fetchall()
	print "\nOutput: Neighborhood, MAX(pop2010)"
	for row in rows:
		print row[0],row[1]
		
		
##########################################
#### Output: Neighborhood, MAX(pop2010), Scientific
##########################################
with con:
	cur = con.cursor()    
	cur.execute("SELECT p.neighborhood, MAX(p.pop2010), e.jobScientific FROM popANDdensity p, employment e WHERE p.neighborhood = e.neighborhood AND p.pop2010=(SELECT MAX(p.pop2010)FROM popANDdensity p)")
	rows = cur.fetchall()
	print "\nOutput: Neighborhood, MAX(pop2010), Scientific"
	for row in rows:
		print row[0],row[1],row[2] 
