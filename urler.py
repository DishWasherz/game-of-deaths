# Gets all pages with a list of dead characters in the wiki

import bs4
from bs4 import BeautifulSoup
import urllib2



def liens():

	url='http://gameofthrones.wikia.com/wiki/Category:Status:_Dead?display=page&sort=mostvisited'
	
	liste_url=[]
	liste_url.append(url)
	print "hello"
	i=0

	while i==0:
		url=liste_url[-1]
		url=urllib2.urlopen(url)
		soup=BeautifulSoup(url)

		taille=len(liste_url)
		listes=soup.findAll("a",{"title":"Category:Status: Dead"})
		listes=set(listes)
		for liste in listes:
			test=BeautifulSoup(liste.prettify()).get_text()
			test = test.encode('utf-8')
			test = test.replace('\n','')
			if test==' next 200':
				url2=[]
	
				for attr,value in BeautifulSoup(liste.prettify()).find('a').attrs.iteritems():
					url2.append(value)

				liste_url.append('http://gameofthrones.wikia.com'+url2[0])
		
		taille2=len(liste_url)
		if taille==taille2:
			i=1
	print liste_url
 	return liste_url


def main():
	liens()


if __name__ == "__main__":
	main()