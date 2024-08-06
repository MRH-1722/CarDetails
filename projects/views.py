from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Detail
from .forms import DetailForm

def details(request):
    allDetails = Detail.objects.all()
    return render(request , 'details.html' , {'allDetails' : allDetails} )

def detail(request, pk): 
    detailObj = Detail.objects.get(uuid=pk)
    variant = Detail.objects.all()
    return render(request, 'detail.html' , {'detail' : detailObj , 'variant':variant})

def createDetail(request):
    form = DetailForm()
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details')
    context = {'form' : form}
    return render(request, 'detail_form.html' , context)

def updateDetail(request, pk):
    detail = Detail.objects.get(uuid=pk)
    form = DetailForm(instance=detail)
    if request.method == 'POST':
        form = DetailForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return redirect('details')
    context = {'form':form}
    return render(request, 'detail_form.html' , context)

def deleteDetail(request , pk):
    detail = Detail.objects.get(uuid=pk)
    if request.method == 'POST':
        detail.delete()
        return redirect('details')
    context = {'detail' : detail}
    return render(request , 'delete_detail.html' , context)
 