import pika
from recorder import AudioRecorder

QUEUE_NAME = "recorder"
HOST = "localhost"

def callback(ch, method, properties, body):
    print(f"[x] Task in the queue {body}")
    recorder = AudioRecorder(body)
    recorder.create()




def __name__ == '__main__':
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=HOST),
    )
    channel = connection.channel()
    channel.queue.declare(queue=QUEUE_NAME)

    channel.basic_consume(
        queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True
    )
    print("[x] waiting for messages! To exit press CTRL-C")
    channel.start_consuming()
