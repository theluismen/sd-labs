# InsultProducer: A producer that sends new insults to the queue
#  every five seconds.

import pika
import time

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel    = connection.channel()

# Declare a queue
channel.queue_declare(queue='insults')

# Send multiple messages
insults = ["Maricon", "Podemita", "Chimpance"]

for insult in insults:
    # Publish a message
    channel.basic_publish(exchange='', routing_key='insults', body=insult)
    print(f" [x] Sent : {insult}")
    # Simulating a delay in task production
    time.sleep(1)  

# Close connection
connection.close()