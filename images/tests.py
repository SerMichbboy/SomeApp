import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from images.models import Image  
from users.models import CustomUser

@pytest.mark.django_db
class TestImageViewSet:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='password123',
            email='test@example.com'
        )
        self.client.force_authenticate(user=self.user)

    def test_list_images(self):
        # Проверка получения всех изображений
        response = self.client.get(reverse('image-list-create'))
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data, list)  # Проверка, что возвращается список

    def test_create_image(self):
        # Проверка создания нового изображения
        with open('images/images_objs/test_image.jpg', 'rb') as image_file:
            data = {
                'image': image_file,
            }
            response = self.client.post(reverse('image-list-create'), data, format='multipart')
            assert response.status_code == status.HTTP_201_CREATED
            assert Image.objects.filter(title='test_image.jpg').exists()  # Проверка, что изображение создано

    def test_retrieve_image(self):
        # Проверка получения конкретного изображения
        image = Image.objects.filter(title='test_image.jpg').get()
        response = self.client.get(reverse('image-list-create', args=[image.pk]))
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == image.title  # Проверка правильности данных

    def test_update_image(self):
        # Проверка обновления изображения
        image = Image.objects.filter(title='test_image.jpg').first()
        new_data = {
            'title': 'Updated image description'
        }
        response = self.client.put(reverse('image-detail', args=[image.id]), new_data)
        assert response.status_code == status.HTTP_200_OK
        image.refresh_from_db()
        assert image.title == 'Updated image description'  # Проверка обновленного значения

    def test_delete_image(self):
        # Проверка удаления изображения
        image = Image.objects.filter(title='test_image.jpg').first()
        response = self.client.delete(reverse('image-detail', args=[image.id]))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Image.objects.filter(id=image.id).exists()  # Проверка, что изображение удалено
