from django.shortcuts import render
from django.http import HttpResponse

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
    page = 'Car details '
    model = 2003
    context = {'page': page , 'model' : model , 'carDetails' : carDetailList}
    return render(request , 'details.html' , context )

def detail(request, pk): 
    detailObj = None
    for i in carDetailList:
        if i['id'] == pk:
            detailObj = i
    return render(request, 'detail.html' , {'detail' : detailObj})
