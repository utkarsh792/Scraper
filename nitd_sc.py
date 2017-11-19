import requests
import time
import os
from BeautifulSoup import BeautifulSoup
def scrape():
	url = "http://www.nitdgp.ac.in"
	while True:
		response = requests.get(url)
		html = response.content
		soup=BeautifulSoup(html)
		y= soup.find("div",{"class":"col-xs-12 col-md-9"})
		x = y.find("div",{"class":"col-xs-12"})
		file=open("links.txt","w")
		for i in x.findAll('a'):
			if 'all_pdf17' in i['href']:
				file.write("http://	nitdgp.ac.in/")
				file.write(i.get('href'))
				file.write("\n") 
		file.close()
		os.system("gedit links.txt")
		break
		#time.sleep(2)
print ("START\n")
scrape()
