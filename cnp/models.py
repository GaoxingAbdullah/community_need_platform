from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    poster = models.ImageField(null=True, blank=True)
    eventDate = models.DateField(null=True)
    eventTime = models.TimeField(null=True)
    location = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class RequestResource(models.Model):
    userName = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=100, null=True)
    resourceNeed = models.CharField(max_length=200, null=True)
    details = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.resourceNeed
