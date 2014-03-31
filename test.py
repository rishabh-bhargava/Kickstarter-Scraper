from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "https://www.kickstarter.com/"

html = urlopen(BASE_URL+"discover/categories/art").read()
soup = BeautifulSoup(html, "lxml")
titles = [title.find("h2") for title in soup.findAll("div", "project-card")]
links = [BASE_URL[0:len(BASE_URL)-1] + h2.a["href"] for h2 in titles]
#h2 = title.find("h2"), BASE_URL[0:len(BASE_URL)-1] + 
#link = BASE_URL[0:len(BASE_URL)-1] + h2.a["href"]
print links