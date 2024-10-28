from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)  
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True) 
    date_joined = models.DateTimeField(auto_now_add=True)  
    phone_number = models.CharField(max_length=15, null=True, blank=True)  

    # Дополнительные поля, которые вы можете добавить
    address = models.CharField(max_length=255, null=True, blank=True) 
    bio = models.TextField(null=True, blank=True) 
    website = models.URLField(null=True, blank=True)  

    # Статус пользователя
    is_active = models.BooleanField(default=True)  
    is_staff = models.BooleanField(default=False)  
    is_superuser = models.BooleanField(default=False) 

