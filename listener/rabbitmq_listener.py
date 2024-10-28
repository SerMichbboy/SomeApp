import pika
import json
from django.conf import settings

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"Получено сообщение: {message}")
    with open("image_events.log", "a") as log_file:
        log_file.write(f"{message}\n")

def start_listening():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.RABBITMQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue=settings.RABBITMQ_QUEUE)
    channel.basic_consume(queue=settings.RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=True)

    print("Ожидание сообщений из RabbitMQ...")
    channel.start_consuming()

if __name__ == "__main__":
    start_listening()
