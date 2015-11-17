import oauth2 as oauth
import urllib
import simplejson as json
import re
import sqlite3 as lite
import sys
import os 

# Go to https://apps.twitter.com/ to setup a project
consumer_key='f6K2zqqjj5c6DPVr03ailsdVB'
consumer_secret='dXD9Fp6bZ7CUVCwsABZL4eGr85mjlX1wZQLrJGSc4CRMCBDYx3'
access_token_key='342124939-K8XZBlzC6lQK7SLP7kMUaU63qvyRUb9Ms9JQeHR9'
access_token_secret='nCuL0rmy7nuW5dAAGoAciPcDTOMXZK9jMqi45LLHerjik'
consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
token = oauth.Token(key=access_token_key, secret=access_token_secret)
client = oauth.Client(consumer, token)
q = "a" # what you are querying
lat = "40.452454" # latitude 
lng = "79.952352" # longitude 
r = "1000" # radius 
url = """https://api.twitter.com/1.1/search/tweets.json?q=%s&include_entities=true&result_type=recent&count=100&geocode=%s,%s,%smi""" % (q,lat,lng,r)

con = None
directoryForDB = "D:/Workshop/homework/Data Analytics/Lab 7/"
if not os.path.exists(directoryForDB):# If database does not exist, creates items
	os.makedirs(directoryForDB)
directoryForDB = directoryForDB + "twitter.db"
con = lite.connect(directoryForDB)

countnode = 0
countlink = 0
header, fhand = client.request(url, method="GET")
jDoc = json.loads(fhand, encoding='utf8')
with con:
    ids= con.cursor()
    for tweet in jDoc['statuses']:
	#print(json.dumps(tweet, sort_keys=True, indent=4 * ' '))
	stringtweet = json.dumps(tweet, sort_keys=True, indent=4 * ' ')# Get all content of a tweet
	userid = stringtweet.split('"favorite_count"',1)
	mentionid = userid[0].split("user_mentions")# Skip media id
	findIt = re.compile(r'"id_str": "\w*"')
	node0 = findIt.findall(userid[1])# Get all tweet id and user ids
	link0 = findIt.findall(mentionid[1])# Get ids be mentioned in this tweet
	node1 = node0[len(node0)-1].split('": "')# Get tweet owner id
	node = node1[1].replace('"','')# Tweet owner id, node
	mark = 0# Set mark as 0
	for links in link0:# Get ids mentioned in this tweet
	    links = links.split('": "')
	    link = links[1].replace('"','')
	    try:# If links exsist, ignore
	        insertlink = "INSERT INTO link VALUES(%s,%s)"%(node,link)
	        ids.execute(insertlink)
	        countlink = countlink +1
	    except:
	        continue
	    mark = 1# If node has links, set mark as 1
	if mark == 1:# Only add node with links into database
	    try:# If node exsist, ignore
	        insertnode = "INSERT INTO node VALUES(%s)"%(node)
	        ids.execute(insertnode)
	        countnode = countnode +1
	    except:
	       continue

print "Add %d nodes, %d links"%(countnode,countlink) # Count nodes and links every test
