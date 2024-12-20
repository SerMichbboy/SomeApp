from PIL import Image as PILImage
import os

def process_image(file):
    # Создаем директорию uploads, если она не существует
    upload_dir = 'images/images_objs'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # Открываем изображение
    image = PILImage.open(file)

    # Обрезка изображения до квадратного формата 1:1 (по центру)
    min_side = min(image.size)  # Находим минимальную сторону для обрезки
    left = (image.width - min_side) // 2
    top = (image.height - min_side) // 2
    right = left + min_side
    bottom = top + min_side
    image = image.crop((left, top, right, bottom))

    # Получение метаданных
    size = image.size
    resolution = f"{size[0]}x{size[1]}"
    image_size = file.size  # Получаем размер файла в байтах
    image_format = image.format  # Получаем формат изображения
    mode = image.mode  # Получаем режим изображения (например, RGB, L, и т.д.)

    # Преобразование изображения в оттенки серого
    gray_image = image.convert('L')

    # Сохраняем изображение в оттенках серого
    gray_file_path = os.path.join(upload_dir, f'gray_{file.name}')
    gray_image.save(gray_file_path)

    # Создаем объект изображения с метаданными
    image_instance = {
        'title': str(file),
        'file_path': gray_file_path,  # Сохраняем путь к изображению в оттенках серого
        'resolution': resolution,
        'size': image_size,
        'format': image_format,  # Добавляем формат изображения
        'mode': mode,  # Добавляем режим изображения
    }

    return image_instance
