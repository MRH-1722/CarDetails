from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DetailForm, ReviewForm
from django.contrib.auth.decorators import login_required
from .models import Detail , Variant
from .utils import searchProject , paginateDetails


def details(request):
    allDetails , search_query = searchProject(request)
    customRange , allDetails = paginateDetails(request , allDetails, 6)

    
        
    context = {'allDetails' : allDetails , 'search_query' : search_query ,  'customRange' :customRange}
    return render(request , 'details.html' , context )

def detail(request, pk):  
    detailObj = Detail.objects.get(uuid=pk)
    variant = Detail.objects.all()
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.detail = detailObj
        review.owner = request.user.profile
        review.save()
        
    return render(request, 'detail.html' , {'detail' : detailObj , 'variant':variant , 'form' : form})


@login_required(login_url='login')
def createDetail(request):
    profile = request.user.profile
    form = DetailForm()

    if request.method == 'POST':
        form = DetailForm(request.POST , request.FILES)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.owner = profile
            detail.save()
            return redirect('account')
        
    context = {'form' : form}
    return render(request, 'detail_form.html' , context)

@login_required(login_url='login')
def updateDetail(request, pk):
    profile = request.user.profile
    detail = profile.detail_set.get(uuid=pk)
    form = DetailForm(instance=detail)

    if request.method == 'POST':
        form = DetailForm(request.POST, request.FILES, instance=detail )
        if form.is_valid():
            form.save()
            return redirect('account')
        
    context = {'form':form}
    return render(request, 'detail_form.html' , context)

@login_required(login_url='login')
def deleteDetail(request , pk):
    profile = request.user.profile
    detail = profile.detail_set.get(uuid=pk)

    if request.method == 'POST':
        detail.delete()
        return redirect('account')
    
    context = {'object' : detail}
    return render(request , 'delete-form.html' , context)
 