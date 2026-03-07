# InsultBroadcaster: A publisher that sends insults from INSULT list
#  to a pubsubchannel.

import pika
import time

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel    = connection.channel()

# Declare a fanout exchange
channel.exchange_declare(exchange='insultsx', exchange_type='fanout')

# Send multiple messages
insults = ["Maricon", "Podemita", "Chimpance"]

for insult in insults:
    # Publish a message
    channel.basic_publish(exchange='insultsx', routing_key='', body=insult)
    print(f" [x] Sent : {insult}")
    # Simulating a delay in task production
    time.sleep(1)  

# Close connection
connection.close()
