from django.shortcuts import render
from django.http import HttpResponse
from .models import Detail

carDetailList = [
    { 
        'id' : '1',
        'Company' : 'Toyota',
        'Model' : 'Corola',
        'Year' : '2012',
        'Description' : 'This car has outstanding suspension'
    },
    { 
        'id' : '2',
        'Company' : 'Honda',
        'Model' : 'Civic',
        'Year' : '2013',
        'Description' : 'This car is the king for the racing'
    }, 
    { 
        'id' : '3',
        'Company' : 'Toyota',
        'Model' : 'Prius',
        'Year' : '2014',
        'Description' : 'This car has outstanding fuel efficiency'
    },
]

def details(request):
    allDetails = Detail.objects.all()
    return render(request , 'details.html' , {'allDetails' : allDetails} )

def detail(request, pk): 
    detailObj = Detail.objects.get(uuid=pk)
    variant = Detail.objects.all()
    return render(request, 'detail.html' , {'detail' : detailObj , 'variant':variant})
