from django.db import models

# Create your models here.
class Skill(models.Model):
    name= models.CharField(max_length=30)
    icon= models.URLField(blank=True, null=True, max_length=400)
    
    def __str__(self) -> str:
        return self.name
    
class Project(models.Model):
    image= models.URLField(blank=True, null=True, max_length=400)
    name= models.CharField(max_length=150)
    overview= models.TextField(blank=True, null=True)
    live_link= models.URLField(max_length=400)
    github_link= models.URLField(max_length=400)
    
    def __str__(self) -> str:
        return self.name
    
class Contact(models.Model):
    name= models.CharField(max_length=10)
    link= models.URLField(max_length=250)
    
    def __str__(self) -> str:
        return self.name
    

class Phone(models.Model):
    number= models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return self.number
    
class Email(models.Model):
    address= models.EmailField()
    
    def __str__(self) -> str:
        return self.address
