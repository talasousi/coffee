from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Coffee(models.Model):
	user = models.ForeignKey(User, default=1)
	beans= models.CharField(max_length=20)
	roast= models.CharField(max_length=20)
	syrup= models.CharField(max_length=20)
	powder= models.CharField(max_length=20)
	espresso= models.IntegerField()
	foam = models.BooleanField(default=False)
	milk = models.BooleanField(default=False)
	water= models.BooleanField(default=False)
	extra= models.TextField()
	name= models.CharField(max_length=20)
