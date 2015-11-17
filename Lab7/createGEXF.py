import os
import sqlite3 as lite

fileline = list()
directory = "D:/Workshop/homework/Data Analytics/Lab 7/"
if not os.path.exists(directory):# If directory does not exist, creates items
	os.makedirs(directory)
directoryForTXT = directory + "twitter.txt"# TXT name
fileread = open(directoryForTXT,"r")# Open TXT
for line in fileread:# Read file in each line, and append into fileline list
    fileline.append(line)

con = None
directoryForDB = directory + "twitter.db"
con = lite.connect(directoryForDB)# Connect database

countnode = 0
countlink = 0
getDB = con.cursor()
getDB.execute("SELECT * FROM node")# Get nodes from database
nodes = getDB.fetchall()
getDB.execute("SELECT * FROM link")# Get links from database
links = getDB.fetchall()
for node in nodes:# Insert nodes into fileline list
    fileline.insert(8,'			<node id="%s" label="%s"/>\n'%(node[0],node[0]))
    countnode= countnode + 1
for link in links:# Insert links into fileline list
    fileline.insert(len(fileline)-3,'			<edge source="%s" target="%s"/>\n'%(link[0],link[1]))
    countlink = countlink + 1    

directoryForGEXF = directory + "twitter.GEXF"# GEXF name
fileupdate = open(directoryForGEXF,"w")# Open GEXF
fileupdate.writelines(fileline)# Rewrite file base on fileline list(with nodes and links)
fileupdate.close()
print "Nodes: %s. Links: %s"%(countnode, countlink)
