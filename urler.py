# Gets all pages with a list of dead characters in the wiki

import bs4
from bs4 import BeautifulSoup
import urllib2



def liens():
	# Setting the url for the first page containing the list of dead characters
	url='http://gameofthrones.wikia.com/wiki/Category:Status:_Dead?display=page&sort=mostvisited'
	
	liste_url=[]
	liste_url.append(url)
	# printing text in the cmd line to show the process has started
	print "hello"
	i=0

	while i==0:
		url=liste_url[-1]
		url=urllib2.urlopen(url)
		soup=BeautifulSoup(url)
		# Looking for the link to the next page with a list of dead characters
		taille=len(liste_url)
		listes=soup.findAll("a",{"title":"Category:Status: Dead"})
		listes=set(listes)
		for liste in listes:
			test=BeautifulSoup(liste.prettify()).get_text()
			test = test.encode('utf-8')
			test = test.replace('\n','')
			# text field next 200 means the hyperlink is the link to the next page
			if test==' next 200':
				url2=[]
				# getting the link
				for attr,value in BeautifulSoup(liste.prettify()).find('a').attrs.iteritems():
					url2.append(value)
				# preparing the link for further analysis, by starting the loop again
				liste_url.append('http://gameofthrones.wikia.com'+url2[0])
		# setting the loop to end when no URL has been added during the last loop
		taille2=len(liste_url)
		if taille==taille2:
			i=1

 	return liste_url


def main():
	liens()


if __name__ == "__main__":
	main()