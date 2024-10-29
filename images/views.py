import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from images.models import Image
from .serializers import ImageSerializer
from django.http import FileResponse
from .services import process_image 
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
# from utils.rabbitmq.rabbitmq import send_rabbitmq_message 

class ImageView(APIView):
    '''
        Въюсет по работе с изображениями.        
    '''
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES.get('image')
        if not file:
            return Response({"error": "No image provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Обработка изображения
        image_instance = process_image(file)
        
        # Сохраняем объект изображения в базе данных
        image_instance_model = Image(
            title=image_instance['title'],
            file_path=image_instance['file_path'],
            size=image_instance['size'],
            resolution=image_instance['resolution'],
        )
        image_instance_model.save()

        # Отправка события в RabbitMQ
        # send_rabbitmq_message("upload", image_instance_model.id)

        return Response(
            data = ImageSerializer(image_instance_model).data, 
            status=status.HTTP_201_CREATED
        )

    def get(self, request, pk=None):
        if pk:
            image = get_object_or_404(Image, pk=pk)

            # Если запрос содержит параметр metadata=true, возвращаем метаданные изображения
            if request.query_params.get('metadata') == 'true':
                serializer = ImageSerializer(image)
                return Response(serializer.data, status=status.HTTP_200_OK)

            # Иначе возвращаем файл изображения
            file_path = image.file_path
            if not os.path.exists(file_path):
                return Response(status=status.HTTP_404_NOT_FOUND)

            response = FileResponse(open(file_path, 'rb'), as_attachment=True)
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
        else:
            images = Image.objects.all()
            serializer = ImageSerializer(images, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ImageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Отправка события в RabbitMQ
            # send_rabbitmq_message("update", image.id)

            return Response(serializer.data)
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if os.path.exists(image.file_path):
            os.remove(image.file_path)

        image.delete()

        # Отправка события в RabbitMQ
        # send_rabbitmq_message("delete", pk)

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
