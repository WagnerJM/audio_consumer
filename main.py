import pika
from recorder.recorder import AudioRecorder

QUEUE_NAME = "recorder"
HOST = "localhost"

def callback(ch, method, properties, body):
    """
    Callback function for consuming the queue
    """
    print(f"[x] Task in the queue {body}")
    # Creating instance of AudioRecorder
    recorder = AudioRecorder(body)
    recorder.create()




if __name__ == '__main__':
    # Connecting to rabbitMQ Server
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=HOST),
    )
    # Creating channel
    channel = connection.channel()
    # Listening on queue=QUEUE_NAME
    channel.queue_declare(queue=QUEUE_NAME)

    # Callback when message is in the queue
    channel.basic_consume(
        queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True
    )

    print("[x] waiting for messages! To exit press CTRL-C")
    # Start the server and listen to events
    channel.start_consuming()
