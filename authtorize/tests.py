import pytest
from rest_framework import status  # Убедитесь, что этот импорт есть
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from authtorize.models import UserToken

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    return User.objects.create_user(
        username='testuser',
        email='testuser@example.com',
        password='testpassword'
    )

@pytest.fixture
def user_token(user):
    return UserToken.objects.create(user=user)

def test_token_obtain(api_client, user):
    assert User.objects.filter(username='testuser').exists()

    response = api_client.post('/api/token/create/', {
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data
    assert UserToken.objects.filter(user=user).exists()

# def test_token_refresh(api_client, user, user_token):
#     assert User.objects.filter(username='testuser').exists()

#     # Получаем токены
#     response = api_client.post('/api/token/create/', {
#         'username': 'testuser',
#         'password': 'testpassword'
#     })

#     assert response.status_code == status.HTTP_200_OK
#     refresh_token = response.data['refresh']

#     # Аутентификация пользователя с использованием access_token
#     api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])

#     # Обновляем токен
#     response = api_client.post('/api/token/refresh/', {
#         'refresh': refresh_token
#     })

#     assert response.status_code == status.HTTP_200_OK
#     assert 'access' in response.data
#     assert user_token.access_token != response.data['access']  

#     # Проверяем, что токен обновлен в базе данных
#     updated_user_token = UserToken.objects.get(user=user)
#     assert updated_user_token.access_token == response.data['access']


def test_logout(api_client, user, user_token):
    assert User.objects.filter(username='testuser').exists()

    # Аутентификация пользователя
    api_client.force_authenticate(user=user)

    response = api_client.post('/api/token/delete/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['message'] == 'Logout successful.'
    assert not UserToken.objects.filter(user=user).exists()

def test_logout_no_token(api_client, user):
    # Пытаемся выйти без аутентификации
    response = api_client.post('/api/token/delete/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED  # Ожидаем 401
    assert 'detail' in response.data  # Проверяем наличие ключа
    assert response.data['detail'] == 'Authentication credentials were not provided.'  # Проверяем сообщение
