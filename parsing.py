# -*-coding:utf-8 -*
import bs4
from bs4 import BeautifulSoup
import urllib2
import urler
import xlwt
import urllib
import simplejson
import json

# creating an excel workbook
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Data')

# exctracting the URL for each character
def parse():
	liste_urls=[]
	#using the function defined in the urler script to get all pages with a list of dead characters
	urls = urler.liens()
	# getting the list of all the interesting elements in the page
	for url in urls:
		soup = BeautifulSoup(urllib2.urlopen(url))
		soup = soup.find_all('tr')
		soup = soup[0].encode('utf-8')
		soup = (BeautifulSoup(soup)).find_all('a')
		for i in range(len(soup)):
			b=[]
			a=BeautifulSoup(soup[i].prettify())
			# extracting URL from the element
			for attr,value in a.find("a").attrs.iteritems():
				b.append(value)
			liste_urls.append(b[0])
	print len(liste_urls)
	return liste_urls


# function to sort and remove the characters that do not have an episode showing their death i.e. dead off-screen, and characters from the Telltale video game
def perso_link_filter(liste_urls):
	j=1
	k=0
	while k <= len(liste_urls):
		soup=urllib2.urlopen('http://gameofthrones.wikia.com'+liste_urls[k])
		soup=BeautifulSoup(soup)
		soup=soup.findAll("aside",{"class":"portable-infobox pi-background pi-theme-wikia pi-layout-default"})
		soup=BeautifulSoup(soup[0].prettify())
		soup=soup.find_all('h3')
		i=0
		for infos in soup:
			infos=BeautifulSoup(infos.prettify())
			infos=infos.encode('utf-8')
			infos = infos.replace('\n','')
			infos = BeautifulSoup(infos).get_text()
			if infos==' Death shown in episode':
				i=1
		if i==0:
			liste_urls.remove(liste_urls[k])
			# print "NO"
		elif i == 1:
			# print "YES"
			k = k + 1
		if j%20 == 0:
			print j
		j += 1
		if len(liste_urls) == k:
			break
	print len(liste_urls)
	return liste_urls


# extracting info from each dead character
def extract(liste_urls):
	count=1
	data=[]
	for url in liste_urls:
		character = ["Name", "House", "Death", "Episode", "First", "Last", "Religion"]
		soup=urllib2.urlopen('http://gameofthrones.wikia.com'+url)
		# cleaning the character's name for the dataset
		urly = url.encode('utf-8')
		urly = urly.replace('_',' ')
		urly = urly.replace('/wiki/' , '')
		character[0] = urly
		urly = urly.replace(' ','_')
		# replacing blank spaces in the name to extract and store pictures easily
		urly = "C:/Users/Alexis/Documents/Home/Projects/GoTDataviz/pics/" + urly + ".jpg"
		errors = []
		soup=BeautifulSoup(soup)
		soup=soup.findAll("aside",{"class":"portable-infobox pi-background pi-theme-wikia pi-layout-default"})
		soup=BeautifulSoup(soup[0].prettify())
		soupy =soup.findAll("div", {"class":"pi-item pi-data pi-item-spacing pi-border-color"})
		# getting the picture
		soupa = soup.findAll("figure" , {"class":"pi-item pi-image"})
		if len(soupa) > 0:
			soupa = soupa[0]
			soupa = set(soupa)
			urla=[]
			levier = 0
			for i in range(len(soupa)):
				if len(list(soupa)[i]) > 1:
					if levier == 0:
						for attr,value in BeautifulSoup(list(soupa)[i].prettify(), "lxml").find('a').attrs.iteritems():
							urla.append(value)
							levier = levier + 1
					else:
						break
			# URL for the picture
			urlo = urla[0]
			# retrieving the picture
			urllib.urlretrieve(urlo, urly)
		# getting the info about the character
		for i in range(len(soupy)):
			info=soupy[i].findAll("h3")
			if len(info) == 0:
				errors.append(url)
			else:
				info = info[0]
				info=BeautifulSoup(info.prettify())
				info=info.encode('utf-8')
				info = info.replace('\n','')
				info=BeautifulSoup(info).get_text()
				if info==' Allegiance':
					infos2 = soupy[i].findAll("div" , {"class":"pi-data-value pi-font"})
					character[1]=BeautifulSoup(infos2[0].prettify()).get_text().replace('\n','')
				elif info==' Death':
					infos2 = soupy[i].findAll("div" , {"class":"pi-data-value pi-font"})
					character[2]=BeautifulSoup(infos2[0].prettify()).get_text().replace('\n','')
				elif info==' Death shown in episode':
					infos2 = soupy[i].findAll("div" , {"class":"pi-data-value pi-font"})
					character[3]=BeautifulSoup(infos2[0].prettify()).get_text().replace('\n','')
				elif info == ' First seen':
					infos2 = soupy[i].findAll("div" , {"class":"pi-data-value pi-font"})
					character[4]=BeautifulSoup(infos2[0].prettify()).get_text().replace('\n','')
				elif info == ' Last seen':
					infos2 = soupy[i].findAll("div" , {"class":"pi-data-value pi-font"})
					character[5]=BeautifulSoup(infos2[0].prettify()).get_text().replace('\n','')
				elif info == ' Religion':
					infos2 = soupy[i].findAll("div" , {"class":"pi-data-value pi-font"})
					character[6]=BeautifulSoup(infos2[0].prettify()).get_text().replace('\n','')
		for j in range(len(character)):
			sheet.write(count, j, character[j])
		data.append(character)
		# print character
		print count
		count = count + 1
	print "errors", errors
	# saving the results in a text file
	# f = open('output.txt','w')
	# simplejson.dump(data, f)
	# f.close()



def main():
	# Create the excel
	header = ["Name", "House", "Death", "Episode", "First", "Last", "Religion"]
	for i in range(len(header)):
		sheet.write(0, i, header[i])
	# Now for the actual parsing
	parsy = parse()
	parsy = perso_link_filter(parsy)
	parsy = extract(parsy)
	workbook.save('World.xls')



if __name__ == "__main__":
	main()