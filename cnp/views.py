from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

# Create your views here.

def index(request):
    return render(request, "index.html")

def resources(request):
    return render(request, 'resources.html')

def requestResources(request):
    return render(request, 'request-resources.html')

def events(request):
    #get all events
    events = Event.objects.all()
    context = {"events": events}
    
    return render(request, 'events.html', context)

def community(request):
    return render(request, 'events.html')

def about(request):
    return render(request, 'events.html')
