from django.urls import path
from . import views

urlpatterns = [
    path('' , views.details ,name="details" ),
    path('detail/<str:pk>/' , views.detail ,name="detail" ),
]

