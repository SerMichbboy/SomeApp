import os
from django.core.wsgi import get_wsgi_application

# Убедитесь, что указываете правильное имя проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()
