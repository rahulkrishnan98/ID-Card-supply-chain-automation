from django.db import models
from django_countries.fields import CountryField
import os

# Create your models here.

def autoincremet():
    num = ClientDetail.objects.count()
    if num == None:
        return 1
    else:
        return num + 1

def autoincremetorder():
    num = OrderDetail.objects.count()
    if num == None:
        string = 'OD'+'0'*(8-len(str(num)))+str(num)
        return string
    else:
        num = num + 1
        string = 'OD'+'0'*(8-len(str(num)))+str(num)
        return string

class ClientDetail(models.Model):
    clientid = models.IntegerField(primary_key=True,blank=False,unique=True,default=autoincremet)
    company = models.CharField(blank=False,max_length=100,default='',unique=True)
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

class OrderDetail(models.Model):
    company = models.ForeignKey(ClientDetail,on_delete=models.CASCADE)
    orderid = models.CharField(blank=False,max_length=100,default=autoincremetorder)
    template = models.BooleanField(default=False)
    data = models.BooleanField(default=False)
    billing = models.BooleanField(default=False)
    production = models.BooleanField(default=False)
    shipping = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.orderid

class Uploadtemplate(models.Model):
    orderid = models.OneToOneField(OrderDetail,on_delete=models.CASCADE,unique=True)
    fimage = models.ImageField(upload_to="static/template/",default="static/template/demo1.jpg")
    bimage = models.ImageField(upload_to="static/template/",default="static/template/demo2.jpg")
    response = models.BooleanField(default=False)

    def __str__(self):
        return self.orderid.orderid

class GetData(models.Model):
    orderid = models.OneToOneField(OrderDetail,on_delete=models.CASCADE,unique=True)
    file = models.FileField(upload_to='static/files/',blank=True)

    def __self__(self):
        return self.orderid.orderid
    def filename(self):
        return os.path.basename(self.file.name)
