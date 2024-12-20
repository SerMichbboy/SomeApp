from django.urls import path
from authtorize.views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    LogoutView,
)

urlpatterns = [
    path(
        'create/',
        CustomTokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    path(
        'refresh/',
        CustomTokenRefreshView.as_view(),
        name='refresh_token'
    ),
    path(
        'delete/',
        LogoutView.as_view(),
        name='delete_token'
    ),
]
