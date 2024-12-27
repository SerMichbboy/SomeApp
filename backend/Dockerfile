FROM python:3.11

# Установим рабочую директорию
WORKDIR /app

# Копируем только requirements.txt для лучшего кэширования
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt \
    && apt-get autoremove -y \
    && apt-get clean \

# Копируем остальной код
COPY . /app/

# Открываем порт 8000 для доступа
EXPOSE 8000

# Для разработки
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Или для продакшн:
# CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
