from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    poster = models.ImageField(max_length=200, null=True)
    eventDate = models.DateField(null=True)
    eventTime = models.TimeField(null=True)
    location = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
