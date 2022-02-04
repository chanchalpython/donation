from django.db import models

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class City(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Bgroup(models.Model):
    bname=models.CharField(max_length=100)
    def __str__(self):
        return self.bname

class Booking(models.Model):
    name=models.CharField(max_length=250)
    age=models.IntegerField()
    address=models.CharField(max_length=250)
    country=models.ForeignKey(Country,on_delete=models.SET_NULL,blank=True,null=True)
    city=models.ForeignKey(City,on_delete=models.SET_NULL,blank=True,null=True)
    bgroup=models.ForeignKey(Bgroup,on_delete=models.SET_NULL,blank=True,null=True)
    mob=models.IntegerField()
    def __str__(self):
        return self.name

