from django.db import models

# Create your models here.

class Category(models.Model):
	
	total_pledged = models.IntegerField(default = 0)
	name = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.name


class Project(models.Model):
	
	category = models.ForeignKey(Category)
	name = models.CharField(max_length = 50)
	pledged = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.name