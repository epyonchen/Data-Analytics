import oauth2 as oauth
import urllib
import simplejson as json

# Go to https://apps.twitter.com/ to setup a project
consumer_key='f6K2zqqjj5c6DPVr03ailsdVB'
consumer_secret='dXD9Fp6bZ7CUVCwsABZL4eGr85mjlX1wZQLrJGSc4CRMCBDYx3'
access_token_key='342124939-K8XZBlzC6lQK7SLP7kMUaU63qvyRUb9Ms9JQeHR9'
access_token_secret='nCuL0rmy7nuW5dAAGoAciPcDTOMXZK9jMqi45LLHerjik'
consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
token = oauth.Token(key=access_token_key, secret=access_token_secret)
client = oauth.Client(consumer, token)
q = "food" # what you are querying
lat = "40.452454" # latitude 
lng = "79.952352" # longitude 
r = "1000" # radius 
url = """https://api.twitter.com/1.1/search/tweets.json?q=%s&include_entities=true&result_type=recent&geocode=%s,%s,%smi""" % (q,lat,lng,r)
count=0
header, fhand = client.request(url, method="GET")
jDoc = json.loads(fhand, encoding='utf8')
for tweet in jDoc['statuses']:
  # prettify output
	count=count+1
	print(json.dumps(tweet, sort_keys=True, indent=4 * ' '))
print count
