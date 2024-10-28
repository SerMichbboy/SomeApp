# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, verbose_name="Имя") 
    last_name = models.CharField(max_length=30, verbose_name="Фамилия") 
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения") 
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Номер телефона")  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # Возвращает полное имя пользователя
