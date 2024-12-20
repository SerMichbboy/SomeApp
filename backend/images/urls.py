from django.urls import path
from .views import (
    ImageView,
)

urlpatterns = [
    path(
        '',
        ImageView.as_view(), 
        name='image-list-create'
    ),
    path(
        '<int:pk>/',
        ImageView.as_view(),  
        name='image-detail'
    ),

]
