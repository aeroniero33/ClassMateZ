from __future__ import unicode_literals
#from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    date = models.DateField()
    def __str__(self):
		return self.name
	#def __unicode__(self):
		#return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=100)
	website = models.URLField(blank=True)
	id = models.AutoField(primary_key=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	classes = models.ManyToManyField(Class)

	def __str__(self):
		return self.user.username

	def __unicode__(self):
		return self.name

class Place(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    address = models.CharField(max_length=100);
    classes = models.ManyToManyField(Class)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Layout(models.Model):
    layout_id = models.AutoField(primary_key=True)
    class_id = models.OneToOneField(Class, on_delete=models.CASCADE)
    place_name = models.OneToOneField(Place, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='layout_images')
    def __str__(self):
		return self.place_name + ", " + self.class_id

	#def __unicode__(self):
		#return (self.place_name + ", " + self.class_id)


class Zone(models.Model):

    ZONE_NAMES = (
        ('A', 'Zone A'),
        ('B', 'Zone B'),
        ('C', 'Zone C'),
        ('D', 'Zone D'),
    )
    layout = models.OneToOneField(Layout, primary_key = True, on_delete=models.CASCADE)
    users = models.ManyToManyField(UserProfile)
    zone_name = models.CharField(max_length=2, choices=ZONE_NAMES)

    def __str__(self):
		return "Zone name: " + self.zone_name + ", " + self.layout

	#def __unicode__(self):
<<<<<<< HEAD:app/models.py
		#return (self.class_id + ", " + self.layout)
=======
		#return (self.class_id + ", " + self.layout)
>>>>>>> master:ClassMateZ/models.py
