from django.db import models

class Image(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название изображения',
    )
    file_path = models.CharField(
        max_length=255,
        verbose_name='Путь к файлу',
    ) 
    upload_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата загрузки',
    )  
    resolution = models.CharField(
        max_length=20,
        verbose_name='Разрешение изображения',
    )  
    size = models.PositiveIntegerField(
        verbose_name='Размер изображения в байтах'
    )  

    def __str__(self):
        return self.title
