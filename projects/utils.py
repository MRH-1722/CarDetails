from django.db.models import Q
from .models import Detail , Variant
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage

def paginateDetails(request , allDetails, results):
    page = request.GET.get('page')
    paginator  = Paginator(allDetails, results)

    try:
        allDetails = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        allDetails = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        allDetails = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 4)

    if rightIndex > paginator.num_pages:
        rightIndex =  paginator.num_pages

    customRange = range(leftIndex , rightIndex)

    return customRange , allDetails

def searchProject(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query =request.GET.get('search_query')


    variants = Variant.objects.filter(car_variant__icontains=search_query)
    allDetails = Detail.objects.distinct().filter(
        Q(company__icontains = search_query) |
        Q(model__icontains = search_query) |
        Q(description__icontains = search_query) |
        Q(owner__name__icontains = search_query) |
        Q(variant__in=variants)
    )

    return allDetails , search_query