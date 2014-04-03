import os

def populate():
	c = Category(name = "anothertest")
	c.save()


if __name__== '__main__':
	print "doing population stuff"
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projects.settings')
	from projects.models import Category, Project
	populate()