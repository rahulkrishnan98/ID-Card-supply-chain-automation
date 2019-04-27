from django.db import models
from django_countries.fields import CountryField

# Create your models here.

def autoincremet():
    num = ClientDetail.objects.count()
    if num == None:
        return 1
    else:
        return num + 1


class ClientDetail(models.Model):
    clientid = models.IntegerField(primary_key=True,blank=False,unique=True,default=autoincremet)
    company = models.CharField(blank=False,max_length=100,default='')
    email = models.EmailField(max_length=30)
    fname = models.CharField(blank=False,max_length=50)
    lname = models.CharField(blank=False,max_length=50)
    address = models.CharField(blank=False,max_length=50,default='')
    city = models.CharField(blank=False,max_length=50)
    phonenum = models.CharField(max_length=15,unique=True,default='')
    country = CountryField(blank_label='Select Country')
    pincode = models.IntegerField(blank=False,default=None)

    def __str__(self):
        return self.company
