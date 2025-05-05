import datetime
import json

from celery import shared_task

from .models import Tasks

from pika import ConnectionParameters, BlockingConnection

def get_rabbitmq_channel():
    conn_params = ConnectionParameters(host='rabbitmq', port=5672)
    conn = BlockingConnection(conn_params)
    channel = conn.channel()
    channel.queue_declare(queue='tasks')
    return channel

@shared_task
def task_reviewer():
    tasks = Tasks.objects.filter(status=False)
    tasks_display = [task.to_json() for task in tasks if str(datetime.datetime.today().weekday()) in task.repeats_days.split(' ')]
    channel = get_rabbitmq_channel()
    channel.basic_publish(exchange='', routing_key='tasks', body=json.dumps(tasks_display))
    print(f" [x] Sent {tasks_display}")

