# Insultfilter: A consumer that retrieves a text from the Work Queue,
# replaces insults from INSULT list in the text for "CENSORED" and store
# the clean text in a RESULTs list.

import redis

def filter ( insult ):
    insults = ["Retrasada", "Imbecil", "Maricona"]

    censored = insult

    for i in insults:
        censored = censored.replace(i, "CENSORED")

    return censored

# Connect to Redis
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

queue_name = "work_queue"
queue_2 = "filter_queue"
client.delete(queue_2)

print("Insult Filter is filtering insults...")

while True:
    # Blocks indefinitely until a insult is available
    insult = client.blpop(queue_name, timeout=0)
  
    new_insult = filter(insult[1])

    cret = client.rpush(queue_2, new_insult)

    if insult:
        print(f"Got: {insult[1]}")
        print(f"Put: {new_insult}")