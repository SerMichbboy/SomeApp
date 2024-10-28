from PIL import Image as PilImage
from io import BytesIO
from django.core.files.base import ContentFile
from django.utils import timezone 
from .models import Image
import os

def process_image(file):
    img = PilImage.open(file)

    # Преобразуем в оттенки серого
    img_gray = img.convert('L')

    # Определяем размеры для изменения
    sizes = [(100, 100), (500, 500)]
    resized_images = {}

    for size in sizes:
        img_resized = img_gray.resize(size)
        buffered = BytesIO()
        img_resized.save(buffered, format=file.content_type.split('/')[-1])
        resized_images[size] = ContentFile(buffered.getvalue(), name=f"{os.path.splitext(file.name)[0]}_{size[0]}x{size[1]}.{file.content_type.split('/')[-1]}")

    # Сохраняем метаданные
    image_instance = Image()
    image_instance.upload_date = timezone.now()  # Устанавливаем дату загрузки
    image_instance.resolution = f"{img.width}x{img.height}"
    image_instance.size = file.size

    return image_instance, resized_images
