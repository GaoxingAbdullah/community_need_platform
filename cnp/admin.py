from django.contrib import admin
from .models import Event, RequestResource

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    search_fields = ['title', 'location']
    list_display = ['title', 'description', 'poster', 'eventDate', 'eventTime', 'location', 'date_created']
    list_filter = ['eventDate', 'eventTime', 'location']
    
class RequestResourceAdmin(admin.ModelAdmin):
    search_fields = ['resourceNeed', 'details', 'userName', 'email']
    list_display = ['userName', 'email', 'phone', 'resourceNeed', 'details', 'date_created']
    list_filter = ['resourceNeed', 'date_created']
    
    
admin.site.register(Event, EventAdmin)
admin.site.register(RequestResource, RequestResourceAdmin)
