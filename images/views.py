from django.http import FileResponse
import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Image
from .serializers import ImageSerializer
from .services import process_image

class ImageView(APIView):
    def post(self, request):
        file = request.FILES.get('image')  # Получаем файл из запроса
        if not file:
            return Response(
                {"error": "No image provided."},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Обработка изображения
        image_instance, resized_images = process_image(file)

        # Сохраняем оригинальное изображение
        image_instance.title = request.data.get('name', 'Untitled') 
        image_instance.file_path = file.name 
        image_instance.save()

        return Response(
            ImageSerializer(image_instance).data,
            status=status.HTTP_201_CREATED
        )

    def get(self, request, pk=None):
        if pk:  # Если указан ID, возвращаем файл
            try:
                image = Image.objects.get(pk=pk)
            except Image.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            # Путь к файлу изображения
            file_path = image.file_path  # Здесь предполагается, что path хранит путь к файлу

            # Проверяем, существует ли файл
            if not os.path.exists(file_path):
                return Response(status=status.HTTP_404_NOT_FOUND)

            # Возвращаем файл
            response = FileResponse(open(file_path, 'rb'))
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

        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
