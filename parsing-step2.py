# -*-coding:utf-8 -*
import bs4
from bs4 import BeautifulSoup
import urllib2
import urler
import xlwt
import urllib

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Data')

def parse():
	liste_urls=[]
	#liste_noms=[]
	urls = urler.liens()
	for url in urls:
		soup = BeautifulSoup(urllib2.urlopen(url))
		soup = soup.find_all('tr')
		soup = soup[0].encode('utf-8')
		soup = (BeautifulSoup(soup)).find_all('a')
		for i in range(len(soup)):
			b=[]
			a=BeautifulSoup(soup[i].prettify())
			for attr,value in a.find("a").attrs.iteritems():
				b.append(value)
			liste_urls.append(b[0])
			#liste_noms.append(b[1])
	print len(liste_urls)
	return liste_urls#,liste_noms



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
			print "NO"
		elif i == 1:
			print "YES"
			k = k + 1
		print j
		j += 1
		if len(liste_urls) == k:
			break
	print len(liste_urls)
	return liste_urls



def extract(liste_urls):
	count=1
	for url in liste_urls:
		character = ["Name", "House", "Death", "Episode", "First", "Last", "Religion"]
		soup=urllib2.urlopen('http://gameofthrones.wikia.com'+url)
		urly = url.encode('utf-8')
		urly = urly.replace('_',' ')
		urly = urly.replace('/wiki/' , '')
		character[0] = urly
		urly = urly.replace(' ','_')
		urly = "C:\users/alexis/documents/projects/pics/" + urly + ".jpg"
		errors = []
		# url = "http://gameofthrones.wikia.com/wiki/Ramsay_Bolton"
		# soup = urllib2.urlopen(url)
		soup=BeautifulSoup(soup)
		soup=soup.findAll("aside",{"class":"portable-infobox pi-background pi-theme-wikia pi-layout-default"})
		soup=BeautifulSoup(soup[0].prettify())
		soupy =soup.findAll("div", {"class":"pi-item pi-data pi-item-spacing pi-border-color"})
		# recup picture
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
			urlo = urla[0]
			#url de l'image récupérée disponible
			urllib.urlretrieve(urlo, urly)
			#image récupérée
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
		# print character
		print count
		count = count + 1
	print "errors", errors



def main():
	header = ["Name", "House", "Death", "Episode", "First", "Last", "Religion"]
	for i in range(len(header)):
		sheet.write(0, i, header[i])
	parsy = parse()
	parsy = perso_link_filter(parsy)
	parsy = extract(parsy)
	workbook.save('World.xls')



if __name__ == "__main__":
	main()


# from bs4 import BeautifulSoup
# import urllib, urllib2
# # url = "/wiki/Ramsay_Bolton"
# url = "/wiki/Aemond_Targaryen"
# soup=urllib2.urlopen('http://gameofthrones.wikia.com'+url)
# urly = url.encode('utf-8')
# urly = urly.replace('_',' ')
# urly = urly.replace('/wiki/' , '')
# urly = urly.replace(' ','_')
# urly = "C:\users/alexis/documents/projects/pics/" + urly + ".jpg"
# soup=BeautifulSoup(soup, "lxml")
# soup=soup.findAll("aside",{"class":"portable-infobox pi-background pi-theme-wikia pi-layout-default"})
# soup=BeautifulSoup(soup[0].prettify(), "lxml")
# soupy =soup.findAll("div", {"class":"pi-item pi-data pi-item-spacing pi-border-color"})
# soupa = soup.findAll("figure" , {"class":"pi-item pi-image"})
# soupa = soupa[0]
# soupa = set(soupa)
# urla=[]
# levier = 0
# for i in range(len(soupa)):
# 	if len(list(soupa)[i]) > 1:
# 		if levier == 0:
# 			for attr,value in BeautifulSoup(list(soupa)[i].prettify(), "lxml").find('a').attrs.iteritems():
# 				urla.append(value)
# 				levier = levier + 1
# 		else:
# 			break
# urlo = urla[0]
# urllib.urlretrieve(urlo, urly)
