from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "https://www.kickstarter.com/"

html = urlopen(BASE_URL+"discover/categories/art").read()
soup = BeautifulSoup(html, "lxml")
titles = [title.find("h2") for title in soup.findAll("div", "project-card")]
links = [BASE_URL[0:len(BASE_URL)-1] + h2.a["href"] for h2 in titles]
#h2 = title.find("h2"), BASE_URL[0:len(BASE_URL)-1] + 
#link = BASE_URL[0:len(BASE_URL)-1] + h2.a["href"]

#print links

def get_categories():
	html = urlopen(BASE_URL).read()
	soup = BeautifulSoup(html, "lxml")
	categ_list = soup.find("ul", "nav small_type")
	categories = [li.text.encode('ascii', 'ignore').strip() for li in categ_list.findAll("li")]
	print categories
	return categories

def main():
	valid_categories = get_categories()
	while True:
		category = raw_input("Write category" + '\n')
		if category in valid_categories:
			break
		print "Invalid category; try again."




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print '\nGoodbye!'