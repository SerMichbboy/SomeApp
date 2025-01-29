FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt \
    && apt-get autoremove -y \
    && apt-get clean \

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Или для прода:
# CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
