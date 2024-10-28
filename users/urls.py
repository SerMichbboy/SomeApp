from django.urls import path, include
from rest_framework import routers
from .views import CustomUserViewSet 

# Создаем маршрутизатор
router = routers.DefaultRouter()
router.register(r'', CustomUserViewSet) 

urlpatterns = [
    path('', include(router.urls)), 
]
