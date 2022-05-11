from unicodedata import name
from django.shortcuts import render

# Create your views here.
from .models import Animals

def savedata(request):
    Animals.objects.all().delete()
    animalList= {'Lion':'Roar', 'Cat':'Meow'}
    if animalList:
        for key, value in animalList.items():
            uniquedata = Animals.objects.filter(name=key)
            print(uniquedata)
            if uniquedata.count() == 0 :
                animal_obj = Animals.objects.create(name=key, sound=value)
                animal_obj.save()

    # Getting all the stuff from database
    query_results = Animals.objects.all()

    # Creating a dictionary to pass as an argument
    context = { 'query_results' : query_results }

    # Returning the rendered html
    return render(request, "home.html", context)

def deledata(request):
    Animals.objects.all().delete()