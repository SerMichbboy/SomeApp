# views.py
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
        image_instance.name = request.data.get(
            'name',
            'Untitled'
        )
        image_instance.path = file.name  # Путь к файлу
        image_instance.save()
        return Response(
            ImageSerializer(image_instance).data,
            status=status.HTTP_201_CREATED
        )

    def get(self, request, pk=None):
        if pk:  # Если указан ID, вернуть конкретное изображение
            try:
                image = Image.objects.get(pk=pk)
            except Image.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ImageSerializer(image)
            return Response(serializer.data)
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
