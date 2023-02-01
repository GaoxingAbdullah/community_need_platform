from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event
from .form import RequestResourceForm

# Create your views here.

def index(request):
    return render(request, "index.html")

def resources(request):
    return render(request, 'resources.html')

def requestResources(request):
    form = RequestResourceForm()
    
    if request.method == 'POST':
        form = RequestResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community')
        
    context = {"form": form}
    return render(request, 'request-resources.html', context)

def events(request):
    #get all events
    events = Event.objects.all()
    context = {"events": events}
    
    return render(request, 'events.html', context)

def community(request):
    return render(request, 'events.html')

def about(request):
    return render(request, 'events.html')
