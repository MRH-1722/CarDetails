from django.urls import path
from . import views

urlpatterns = [
    path('' , views.details ,name="details" ),
    path('detail/<str:pk>/' , views.detail ,name="detail" ),

    path('create-detail/' , views.createDetail , name="create-detail"),
    path('update-detail/<str:pk>/' , views.updateDetail , name="update-detail"),
    path('delete-detail/<str:pk>/' , views.deleteDetail , name="delete-detail"),
    
]

