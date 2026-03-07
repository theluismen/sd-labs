# InsultConsumer: A consumer that reads new insults from the
#  queue and them to a REDIS list (INSULTS) only if they are new.

import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel    = connection.channel()

# Declare a queue (ensure it exists)
channel.queue_declare(queue='insults')

# Define the callback function
def callback(ch, method, properties, body):
    print(f" [x] Received : {body.decode()}")

# Consume messages
channel.basic_consume(queue='insults', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
