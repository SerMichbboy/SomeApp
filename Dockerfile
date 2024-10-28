# Используем базовый образ Python
FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app/

# Открываем порт для Django
EXPOSE 8000

# Команда запуска Django-сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
