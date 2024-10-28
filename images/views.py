import os
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Image
from .serializers import ImageSerializer
from django.http import FileResponse
from .services import process_image 
from rest_framework.permissions import IsAuthenticated

class ImageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES.get('image')  # Получаем файл из запроса
        if not file:
            return Response(
                {"error": "No image provided."},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Обработка изображения
        image_instance = process_image(file, request.data.get('name', 'Untitled'))
        
        # Сохраняем объект изображения в базе данных
        image_instance_model = Image(
            title=image_instance['title'],
            file_path=image_instance['file_path'],
            size=image_instance['size'],
            resolution=image_instance['resolution'],
        )
        image_instance_model.save()

        return Response(
            ImageSerializer(image_instance_model).data,
            status=status.HTTP_201_CREATED
        )

    def get(self, request, pk=None):
        if pk:  # Если указан ID, вернуть конкретное изображение
            try:
                image = Image.objects.get(pk=pk)
            except Image.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            # Путь к файлу
            file_path = image.file_path
            
            # Проверяем, существует ли файл
            if not os.path.exists(file_path):
                return Response(status=status.HTTP_404_NOT_FOUND)

            # Возвращаем файл как ответ
            response = FileResponse(open(file_path, 'rb'), as_attachment=True)
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
        
        else:  # Если ID не указан, вернуть список всех изображений
            images = Image.objects.all()
            serializer = ImageSerializer(images, many=True)
            return Response(serializer.data)

    def put(self, request, pk):
        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ImageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Удаляем файл с диска
        if os.path.exists(image.file_path):
            os.remove(image.file_path)

        # Удаляем запись из базы данных
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
