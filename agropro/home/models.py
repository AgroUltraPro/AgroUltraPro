from django.db import models

# Create your models here.

class Farmer(models.Model):
    name=models.CharField(max_length=150)
    phone=models.CharField(max_length=10)
    username=models.CharField(max_length=20)
    email=models.EmailField(null=True, blank=True)
    area=models.IntegerField(null=True, blank=True)
    address=models.CharField(max_length=300,null=True, blank=True)
    state=models.CharField(max_length=30,null=True, blank=True)
    #crop=models.ManyToManyField(Crop)

    def _str_(self):
        return self.name

class Wholesaler(models.Model):
    name=models.CharField(max_length=150)
    phone=models.CharField(max_length=10)
    username=models.CharField(max_length=20,null=True)
    email=models.EmailField(null=True, blank=True)
    address=models.CharField(max_length=300,null=True, blank=True)
    state=models.CharField(max_length=30,null=True, blank=True)

    def _str_(self):
        return self.username

class Crop(models.Model):
    name=models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    quantity=models.FloatField()
    available=models.BooleanField()
    price=models.FloatField()
    farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    

    def _str_(self):
        return self.name
    
class Notification(models.Model):
    crop=models.ForeignKey(Crop,on_delete=models.CASCADE)
    wholesaler=models.ForeignKey(Wholesaler,on_delete=models.CASCADE)
    accepted=models.BooleanField()
    interested=models.BooleanField()