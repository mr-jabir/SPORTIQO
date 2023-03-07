from django.db import models

# Create your models here.

class customerdb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    Confirmpassword = models.CharField(max_length=100, null=True, blank=True)

class cartdb(models.Model):
    Proname= models.CharField(max_length=50,null=True,blank=True)
    Category=models.CharField(max_length=100,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)

class checkoutdb(models.Model):
    Name= models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Pincode = models.IntegerField(null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    CardName= models.CharField(max_length=50,null=True,blank=True)
    CreditNo = models.IntegerField(null=True,blank=True)
    Expiration = models.CharField(max_length=100, null=True, blank=True)
    Cvv = models.IntegerField(null=True,blank=True)











