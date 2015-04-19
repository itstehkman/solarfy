from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Customer(models.Model):
	address = models.TextField()
	billJson = models.TextField()
	
	def __str__(self):
		return self.address