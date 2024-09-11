from django.db.models import Q
from .models import Detail , Variant

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