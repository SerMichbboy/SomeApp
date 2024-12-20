import logging
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from images.models import Image  
from users import CustomUser

@pytest.mark.django_db
class TestImageViewSet:
    @pytest.fixture(autouse=True)
    def setup(self):
        """Настройка клиента и аутентификация пользователя перед тестами."""
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='password123',
            email='test@example.com'
        )
        self.client.force_authenticate(user=self.user)

    def test_list_images(self):
        """Тестирование получения списка изображений."""
        response = self.client.get(reverse('image-list-create'))
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data, list)  # Проверка, что возвращается список

    def test_create_image(self):
        """Тестирование создания нового изображения."""
        with open('images/images_objs/test_image.jpg', 'rb') as image_file:
            data = {'image': image_file}
            response = self.client.post(reverse('image-list-create'), data, format='multipart')
            assert response.status_code == status.HTTP_201_CREATED
            assert Image.objects.filter(title='test_image.jpg').exists()

    def test_retrieve_image_metadata(self):
        """Тестирование получения метаданных изображения."""
        with open('images/images_objs/test_image.jpg', 'rb') as image_file:
            response = self.client.post(reverse('image-list-create'), {'image': image_file}, format='multipart')
            assert response.status_code == status.HTTP_201_CREATED
            image_id = response.data['id']
            metadata_response = self.client.get(reverse('image-detail', args=[image_id]), {'metadata': 'true'})
            assert metadata_response.status_code == status.HTTP_200_OK
            assert metadata_response.data['title'] == 'test_image.jpg'

    def test_update_image(self):
        """Тестирование обновления данных изображения."""
        # Создаем изображение
        with open('images/images_objs/test_image.jpg', 'rb') as image_file:
            response = self.client.post(reverse('image-list-create'), {'image': image_file}, format='multipart')
            assert response.status_code == status.HTTP_201_CREATED
            image_id = response.data['id']

        image = Image.objects.get(id=image_id)
        # Подготовка данных для обновления
        new_data = {
            'title': 'Updated image description',
            'file_path': image.file_path, 
            'size': image.size,  
            'resolution': image.resolution  
        }
    
        update_response = self.client.put(reverse('image-detail', args=[image_id]), new_data)
        assert update_response.status_code == status.HTTP_200_OK, update_response.data
        image.refresh_from_db()  # Обновляем объект из БД
        assert image.title == 'Updated image description' 


    def test_delete_image(self):
        """Тестирование удаления изображения."""
        with open('images/images_objs/test_image.jpg', 'rb') as image_file:
            response = self.client.post(reverse('image-list-create'), {'image': image_file}, format='multipart')
            assert response.status_code == status.HTTP_201_CREATED
            image_id = response.data['id']

        delete_response = self.client.delete(reverse('image-detail', args=[image_id]))
        assert delete_response.status_code == status.HTTP_204_NO_CONTENT
        assert not Image.objects.filter(id=image_id).exists()  # Проверка, что изображение удалено
