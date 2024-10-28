from django.urls import path
from .views import (
    ImageView,
    ImageView,
)

urlpatterns = [
    path(
        'images/',
        ImageView.as_view(),
        name='image-list-create'
    ),
    path(
        'images/<int:pk>/',
        ImageView.as_view(),
        name='image-detail'
    ),
]
