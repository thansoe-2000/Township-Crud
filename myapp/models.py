from django.db import models

# Create your models here.

class Township(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Village(models.Model):
    township = models.ForeignKey(Township, on_delete=models.CASCADE)
    schools = models.IntegerField(max_length=200, blank=True)
    houses = models.IntegerField(max_length=200, blank=True)
    populations = models.IntegerField(max_length=200, blank=True)
    monestaries = models.IntegerField(max_length=200, blank=True)
    name = models.CharField(max_length=200)
   
    
    def __str__(self):
        return self.name

class Town(models.Model):
    township = models.ForeignKey(Township, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Ward(models.Model):
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    schools = models.IntegerField(blank=True, null=True)
    houses = models.IntegerField(blank=True, null=True)
    monestaries = models.IntegerField(blank=True, null=True)
    
    
    def __str__(self):
        return self.name