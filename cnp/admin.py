from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    search_fields = ['title', 'location']
    list_display = ['poster', 'title', 'description', 'eventDate', 'eventTime', 'location', 'date_created']
    list_filter = ['eventDate', 'eventTime', 'location']
    
admin.site.register(Event, EventAdmin)
