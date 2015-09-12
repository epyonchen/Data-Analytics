# -*- coding: utf-8 -*-
import csv                                   ### Programed by Epyon ###
import urllib

PopulationAndDensity = "http://boxnumbertwo.com/PittsburghData/Population_and_Density.csv"

fhand = urllib.urlopen(PopulationAndDensity)

pop1940 = dict()  # Declare every decade as a dict
pop1950 = dict()  # How to build array of structure?
pop1960 = dict()
pop1970 = dict()
pop1980 = dict()
pop1990 = dict()
pop2000 = dict()
pop2010 = dict()
location = list()  # Declare an list to record locations

try:
	reader = csv.reader(fhand)
	next(reader, None)  # skip the headers
	for row in reader:
		pop1940[row[0]] = int(row[2].replace(",",""))  # Every location is a key in dict
		pop1950[row[0]] = int(row[3].replace(",",""))
		pop1960[row[0]] = int(row[4].replace(",",""))
		pop1970[row[0]] = int(row[5].replace(",",""))
		pop1980[row[0]] = int(row[6].replace(",",""))
		pop1990[row[0]] = int(row[7].replace(",",""))
		pop2000[row[0]] = int(row[8].replace(",",""))
		pop2010[row[0]] = int(row[9].replace(",",""))
		location.append(row[0])  # Add locations in list

finally:
	fhand.close()

		
# Calculating total population every decades
count = 0
total = 0
for key in pop1940:
	total = total + pop1940[location[count]]
	count = count + 1
pop1940["total"] = total  # Add total population into each dict    ### Self-Notice ###
                          # I think it is a better structure.      ### Key in dict need ''###
count = 0
total = 0
for key in pop1950:
	total = total + pop1950[location[count]]
	count = count + 1
pop1950["total"] = total

count = 0
total = 0
for key in pop1960:
	total = total + pop1960[location[count]]
	count = count + 1
pop1960["total"] = total

count = 0
total = 0
for key in pop1970:
	total = total + pop1970[location[count]]
	count = count + 1
pop1970["total"] = total

count = 0
total = 0
for key in pop1980:
	total = total + pop1980[location[count]]
	count = count + 1
pop1980["total"] = total

count = 0
total = 0
for key in pop1990:
	total = total + pop1990[location[count]]
	count = count + 1
pop1990["total"] = total

count = 0
total = 0
for key in pop2000:
	total = total + pop2000[location[count]]
	count = count + 1
pop2000["total"] = total

count = 0
total = 0
for key in pop2010:
	total = total + pop2010[location[count]]
	count = count + 1
pop2010["total"] = total


print "Difference between every decades"
print "1940 - 1950: ",pop1950['total'] - pop1940['total']
print "1950 - 1960: ",pop1960['total'] - pop1950['total']
print "1960 - 1970: ",pop1970['total'] - pop1960['total']
print "1970 - 1980: ",pop1980['total'] - pop1970['total']
print "1980 - 1990: ",pop1990['total'] - pop1980['total']
print "1990 - 2000: ",pop2000['total'] - pop1990['total']
print "2000 - 2010: ",pop2010['total'] - pop2000['total']
#Difference between 1940 - 1950:  5148
#Difference between 1950 - 1960:  -61563
#Difference between 1960 - 1970:  -95088
#Difference between 1970 - 1980:  -96216
#Difference between 1980 - 1990:  -54059
#Difference between 1990 - 2000:  -36352
#Difference between 2000 - 2010:  -27823

print "\nDifference between every decades for Mount Washington"
print "1940 - 1950: ",pop1950['Mount Washington'] - pop1940['Mount Washington']
print "1950 - 1960: ",pop1960['Mount Washington'] - pop1950['Mount Washington']
print "1960 - 1970: ",pop1970['Mount Washington'] - pop1960['Mount Washington']
print "1970 - 1980: ",pop1980['Mount Washington'] - pop1970['Mount Washington']
print "1980 - 1990: ",pop1990['Mount Washington'] - pop1980['Mount Washington']
print "1990 - 2000: ",pop2000['Mount Washington'] - pop1990['Mount Washington']
print "2000 - 2010: ",pop2010['Mount Washington'] - pop2000['Mount Washington']
#Difference between 1940 - 1950 for Mount Washington:  -953
#Difference between 1950 - 1960 for Mount Washington:  -1645
#Difference between 1960 - 1970 for Mount Washington:  -2628
#Difference between 1970 - 1980 for Mount Washington:  -2992
#Difference between 1980 - 1990 for Mount Washington:  -1095
#Difference between 1990 - 2000 for Mount Washington:  -822
#Difference between 2000 - 2010 for Mount Washington:  -1079

print "\nDifference between every decades for North Oakland"
print "1940 - 1950: ",pop1950['North Oakland'] - pop1940['North Oakland']
print "1950 - 1960: ",pop1960['North Oakland'] - pop1950['North Oakland']
print "1960 - 1970: ",pop1970['North Oakland'] - pop1960['North Oakland']
print "1970 - 1980: ",pop1980['North Oakland'] - pop1970['North Oakland']
print "1980 - 1990: ",pop1990['North Oakland'] - pop1980['North Oakland']
print "1990 - 2000: ",pop2000['North Oakland'] - pop1990['North Oakland']
print "2000 - 2010: ",pop2010['North Oakland'] - pop2000['North Oakland']
#Difference between 1940 - 1950 for North Oakland:  1936
#Difference between 1950 - 1960 for North Oakland:  -610
#Difference between 1960 - 1970 for North Oakland:  1213
#Difference between 1970 - 1980 for North Oakland:  42
#Difference between 1980 - 1990 for North Oakland:  2128
#Difference between 1990 - 2000 for North Oakland:  -979
#Difference between 2000 - 2010 for North Oakland:  694

print "\nDifference between every decades"	
print "1940 - 1950: ",pop1950['Shadyside'] - pop1940['Shadyside']
print "1950 - 1960: ",pop1960['Shadyside'] - pop1950['Shadyside']
print "1960 - 1970: ",pop1970['Shadyside'] - pop1960['Shadyside']
print "1970 - 1980: ",pop1980['Shadyside'] - pop1970['Shadyside']
print "1980 - 1990: ",pop1990['Shadyside'] - pop1980['Shadyside']
print "1990 - 2000: ",pop2000['Shadyside'] - pop1990['Shadyside']
print "2000 - 2010: ",pop2010['Shadyside'] - pop2000['Shadyside']
#Difference between 1940 - 1950:  1599
#Difference between 1950 - 1960:  -1102
#Difference between 1960 - 1970:  -2329
#Difference between 1970 - 1980:  -1903
#Difference between 1980 - 1990:  -560
#Difference between 1990 - 2000:  369
#Difference between 2000 - 2010:  161

#Calculate the difference of population in different location between 1940 and 2010
totalDiff20101940 = dict()
i = -1 #  Why does it start from -1？
for key in pop2010:
  totalDiff20101940[location[i]] = pop2010[location[i]] - pop1940[location[i]]
  i = i+1
totalDiff20101940 = sorted(totalDiff20101940.items(), key=lambda x:x[1])

print "\nDifference in different location between 1940 and 2010:"
print "Top 10 - Worst"  # Wrong answer: Top 11 instead of Top 10.
for key in range(0,10):
    print key+1,totalDiff20101940[key]
print "Top 10 - Best"  # Order of Top 10 - best is wrong.
for key in range(0,10):
    print key+1,totalDiff20101940[89-key]	
#Top 10 - Worst
#  ('South Side Flats', -15879)
#  ('Middle Hill', -15322)
#  ('Crawford-Roberts', -14789)
#  ('Bloomfield', -12266)
#  ('Larimer', -11610)
#  ('Mount Washington', -11214)
#  ('East Allegheny', -10835)
#  ('Homewood South', -10678)
#  ('South Side Slopes', -10660)
#  ('Perry South', -10521)
#  ('Homewood North', -10319)
#Top 10 - Best
#  ('Stanton Heights', -9)
#  ('Bon Air', -6)
#  ('Swisshelm Park', 23)
#  ('Oakwood', 290)
#  ('New Homestead', 301)
#  ('Northview Heights', 552)
#  ('Westwood', 618)
#  ('Squirrel Hill North', 928)
#  ('Windgap', 1151)
#  ('Banksville', 2930)
#  ('North Oakland', 4424)
	
