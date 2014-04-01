from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

BASE_URL = "https://www.kickstarter.com/"

def get_projects(categ_url):
	html = urlopen(categ_url).read()
	soup = BeautifulSoup(html, "lxml")
	titles = [title.find("h2") for title in soup.findAll("div", "project-card")]
	links = [BASE_URL[0:len(BASE_URL)-1] + h2.a["href"] for h2 in titles]
	return links

def get_project_data(project_link):
	html = urlopen(project_link).read()
	soup = BeautifulSoup(html, "lxml")
	name_cont = soup.find("div", "NS-project_-running_board")
	name = name_cont.find("h2").text.encode('ascii', 'ignore').strip()

	money_cont = soup.find("div", "NS_projects__ecom")
	money_pledged = money_cont.find("h5").find_next_sibling("h5").div.data.text.encode('ascii', 'ignore').strip()
	money = ""
	for c in money_pledged:
		if c.isdigit():
			money += c
	return name, money


def get_categories():
	html = urlopen(BASE_URL).read()
	soup = BeautifulSoup(html, "lxml")
	categ_list = soup.find("ul", "nav small_type")
	categories = [(li.text.encode('ascii', 'ignore').strip(), BASE_URL[0:len(BASE_URL)-1] + li.a["href"]) for li in categ_list.findAll("li")]
	#print categories
	return categories

def main():
	valid_categories = get_categories()
	not_found = True
	while not_found:
		category = raw_input("Write category" + '\n')
		for i in xrange(len(valid_categories)):
			if category == valid_categories[i][0]:
				link = valid_categories[i][1]
				not_found = False
		if not_found:
			print "Invalid category; try again."
	print link
	project_links = get_projects(link)
	total_data = []
	total_money = 0
	for p_link in project_links:
		p_data = get_project_data(p_link)
		total_data.append(p_data)
		total_money += float(p_data[1])
	print total_money
	print total_data



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print '\nGoodbye!'