import pika
import json
from django.conf import settings

def send_rabbitmq_message(event_type, image_id):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=settings.RABBITMQ_HOST)
    )
    channel = connection.channel()

    # Объявляем очередь
    channel.queue_declare(queue=settings.RABBITMQ_QUEUE)

    # Создаем сообщение
    message = {
        "event": event_type,
        "image_id": image_id
    }

    # Отправляем сообщение
    channel.basic_publish(
        exchange='',
        routing_key=settings.RABBITMQ_QUEUE,
        body=json.dumps(message)
    )
    connection.close()