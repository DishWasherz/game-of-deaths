# -*-coding:utf-8 -*

import json
import re
import pandas as pd


#episodes and seasons to be done automatically
s1 = ["Winter is Coming", "The Kingsroad", "Lord Snow", "Cripples, Bastards and Broken Things", "The Wolf and the Lion","A Golden Crown","You Win or You Die","The Pointy End","Baelor","Fire and Blood"]
s2 = ["The North Remembers","The Night Lands","What is Dead May Never Die","Garden of Bones","The Ghost of Harrenhal","The Old Gods and the New","A Man Without Honor","The Prince of Winterfell","Blackwater","Valar Morghulis"]
s3 = ["Valar Dohaeris","Dark Wings, Dark Words", "Walk of Punishment","And Now His Watch is Ended","Kissed by Fire", "The Climb","The Bear and the Maiden Fair", "Second Sons","The Rains of Castamere","Mhysa"]
s4 = ["Two Swords","The Lion and the Rose","Breaker of Chains", "Oathkeeper","First of His Name","The Laws of Gods and Men","Mockingbird","The Mountain and the Viper","The Watchers on the Wall","The Children"]
s5 = ["The Wars to Come","The House of Black and White","High Sparrow","Sons of the Harpy","Kill the Boy","Unbowed, Unbent, Unbroken","The Gift","Hardhome","The Dance of Dragons","Mother's Mercy"]
s6 = ["The Red Woman","Home","Oathbreaker","Book of the Stranger","The Door","Blood of My Blood","The Broken Man","No One","Battle of the Bastards","The Winds of Winter"]


#load the file and dump into a list
data_path = 'output.txt'
listy=[]
file = open(data_path, "r")
for line in file:
	try:
		character = json.loads(line)
		listy.append(character)
	except:
		continue

# load the list and check it is intact
listy=listy[0]
print len(listy)
print len(listy[0])
print listy[0]

#filter unwanted chars and fix encoding
#take inverted commas away with replace
#leading/trailing spaces with strip and redundant whitespaces with replace
for i in range(len(listy)):
	for j in range(len(listy[i])):
		listy[i][j]=listy[i][j].encode('utf-8').replace('"','').strip().replace('   ',' ').replace('  ',' ')

#checking data is clean
print listy[0][5]
for i in listy[57]:
	print i

#création du dataframe pandas
daty = pd.DataFrame(listy,columns=["Name", "House", "Death", "Episode", "First", "Last", "Religion"])
print daty



# Attention, le nom du tueur n'est pas donné dans le dataset wikia
# tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
# tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
# tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
