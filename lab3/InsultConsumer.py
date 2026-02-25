import redis

# Connect to Redis
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

queue_name = "insult_queue"
queue_2 = "new_queue"
client.delete(queue_2)

print("Consumer is waiting for insults...")

while True:
    # Blocks indefinitely until a insult is available
    insult = client.blpop(queue_name, timeout=0)
  
    cret = client.sadd(queue_2, insult[1])

    if insult:
        print(f"Consumed: {insult[1]}")
        if cret:
            print(f"Añadido: {insult[1]}")