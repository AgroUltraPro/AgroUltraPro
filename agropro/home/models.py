from django.db import models

# Create your models here.

class Farmer(models.Model):
    name=models.CharField(max_length=150)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    email=models.EmailField(null=True, blank=True)
    area=models.IntegerField(null=True, blank=True)
    address=models.CharField(max_length=300,null=True, blank=True)
    #crop=models.ManyToManyField(Crop)

    def __str__(self):
        return self.name

class Wholesaler(models.Model):
    name=models.CharField(max_length=150)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    email=models.EmailField(null=True, blank=True)
    address=models.CharField(max_length=300,null=True, blank=True)

    def __str__(self):
        return self.name

class Crop(models.Model):
    name=models.CharField(max_length=150)
    quantity=models.IntegerField()
    available=models.BooleanField()
    price=models.FloatField()
    farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
    
class Notification(models.Model):
    crop=models.ForeignKey(Crop,on_delete=models.CASCADE)
    wholesaler=models.ForeignKey(Wholesaler,on_delete=models.CASCADE)
    accepted=models.BooleanField()
    interested=models.BooleanField()

