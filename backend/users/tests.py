import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import CustomUser


@pytest.mark.django_db
class TestCustomUserViewSet:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='password123',
            email='test@example.com'
        )
        self.client.force_authenticate(user=self.user)

    def test_list_users(self):
        response = self.client.get(reverse('customuser-list'))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) > 0

    def test_retrieve_user(self):
        response = self.client.get(reverse(
            'customuser-detail',
            args=[self.user.id])
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data['username'] == self.user.username

    def test_create_user(self):
        data = {
            'username': 'newuser',
            'password': 'password123',
            'email': 'newuser@example.com',
        }
        response = self.client.post(reverse('customuser-list'), data)
        assert response.status_code == status.HTTP_201_CREATED
        assert CustomUser.objects.filter(username='newuser').exists()

    def test_update_user(self):
        # Проверка обновления пользователя
        new_data = {
            'username': 'updateduser'
        }
        response = self.client.put(reverse(
            'customuser-detail',
            args=[self.user.id]
        ), new_data)
        assert response.status_code == status.HTTP_200_OK
        self.user.refresh_from_db()
        assert self.user.username == 'updateduser'

    def test_delete_user(self):
        # Проверка удаления пользователя
        response = self.client.delete(reverse(
            'customuser-detail',
            args=[self.user.id])
        )
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not CustomUser.objects.filter(id=self.user.id).exists()
