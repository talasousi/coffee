from django.db import models
from django.contrib.auth.models import User

class Bean(models.Model):
	name= models.CharField(max_length=20)
	price= models.DecimalField(max_digits=6, decimal_places=3)

class Roast(models.Model):
	name= models.CharField(max_length=20)
	price= models.DecimalField(max_digits=6, decimal_places=3)

class Syrup(models.Model):
	name= models.CharField(max_length=20)
	price= models.DecimalField(max_digits=6, decimal_places=3)

class Powder(models.Model):
	name= models.CharField(max_length=20)
	price= models.DecimalField(max_digits=6, decimal_places=3)


class Coffee(models.Model):
	user= models.ForeignKey(User, default=1)
	name= models.CharField(max_length=20)
	beans= models.ForeignKey(Bean)
	roast= models.ForeignKey(Roast)
	syrup= models.ManyToManyField(Syrup)
	powder= models.ManyToManyField(Powder)
	water= models.BooleanField(default=False)
	foam= models.BooleanField(default=False)
	milk= models.BooleanField(default=False)
	shot= models.PositiveIntegerField(default=0)
	extra= models.TextField()
	price= models.DecimalField(max_digits=6, decimal_places=3, default=0)
	
