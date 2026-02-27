# AngryProducer: A producer that sends a text with insults to a Work
# Queue every 3 seconds

import redis
import time

# Connect to Redis
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

queue_name = "work_queue"

# Send multiple messages
insults = ["Retrasada", "Imbecil", "Maricona"]

for insult in insults:
    client.rpush(queue_name, f"Eres una persona {insult}")
    print(f"Produced: {insult}")
    time.sleep(3)  # Simulating a delay in task production
