from django.db import models
from datetime import datetime
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    firstName = models.CharField(max_length=200, null=True, blank=True)
    lastName = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.DateField()
    country = CountryField()
    profession = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(upload_to="images", null=True, blank=True)
    adress = models.CharField(max_length=200, null=True, blank=True)
    phoneNumber = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.firstName
    

    