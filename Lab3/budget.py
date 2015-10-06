################################
### Creates Database
### Updates Database with Data
################################

from BeautifulSoup import *
import urllib
import os
import sqlite3 as lite
import sys


siteHTML = "http://boxnumbertwo.com/MovieData/budget.html"
html = urllib.urlopen(siteHTML).read()
soup = BeautifulSoup(html)
table = soup.findAll("table")
moviesPB = dict()
moviesDG = dict()
moviesWG = dict()
count = 0
table = str(table)
table = table.split("</tr><tr>\n</tr><tr>") #  Split each movie
for row in table:

    temp = row.split("</td>")
    name = temp[2].split('summary">') #  Get movies' name
    name = name[1].strip("</a></b>")
    PB = temp[3].split('<td class="data">$',) #  Get movies' production budget
    PB = int(PB[1].replace(",",""))
    moviesPB[name] = PB
    DG = temp[4].split('<td class="data">$',) #  Get movies' domestic gross
    DG = int(DG[1].replace(",",""))
    moviesDG[name] = DG
    WG = temp[5].split('<td class="data">$',) # Get movies' worldwide gross
    WG = int(WG[1].replace(",",""))
    moviesWG[name] = WG
    #print count
    #count = count +1
    #if count >5:
      # break
    
## Set directory to computer
directoryForDB = "D:/Workshop/homework/Data Analytics/Lab3/"
if not os.path.exists(directoryForDB):
	os.makedirs(directoryForDB)

directoryForDB = directoryForDB + "movies.db"
## If database does not exist, creates items
## If database does exist, opens it
con = lite.connect(directoryForDB)
with con:
	budgetdb = con.cursor()
	for key in moviesPB:
	        keys = "%" + key + "%" #  Search name with part of key words
	        insertStatement = 'UPDATE MoviesInfo SET PB = %d, DG = %d, WG = %d WHERE name like "%s"' % (moviesPB[key],moviesDG[key],moviesWG[key],keys) #  Add movies' names and ratings into database
		budgetdb.execute(insertStatement)
		#insertStatement = 'DELETE FROM MoviesInfo WHERE PB="NULL"'
		#budgetdb.execute(insertStatement)
		print count
		count = count +1
		#print keys
		#if count>5:
		  #break
	## NEEDED, if not, database does not update
	con.commit()
