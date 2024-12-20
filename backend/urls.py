from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', include('authtorize.urls')),
    path('api/users/', include('users.urls')),
    path('api/images/', include('images.urls')),
]