# InsultProducer: A producer that sends new insults to the queue
# every five seconds.

import redis
import time

# Connect to Redis
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

queue_name = "insult_queue"

# Send multiple messages
insults = ["Maricon", "Podemita", "Chimpance"]

for insult in insults:
    client.rpush(queue_name, insult)
    print(f"Produced: {insult}")
    time.sleep(1)  # Simulating a delay in task production
