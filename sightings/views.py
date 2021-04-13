from django.shortcuts import render
from django.http import HttpResponse
from .models import Sighting

def base_view(request):
    return render(request,'sightings/base.html', {})

def map(request):
    sightings = Sighting.objects.all()[:100]
    context = {
            'sightings':sightings,
            }
    return render(request,'sightings/map.html',context)

def list(request):
    pass

def update(request,Unique_Squirrel_Id):
    pass

def add(request):
    pass

def stats(request):
    pass


