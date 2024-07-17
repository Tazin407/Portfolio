from django.db import models

# Create your models here.
class skill(models.Model):
    name= models.CharField(max_length=30)
    
class project(models.Model):
    image= models.URLField(blank=True, null=True, max_length=400)
    name= models.CharField(max_length=150)
    overview= models.TextField()
    live_link= models.URLField(max_length=400)
    
