# InsultBroadcaster: A publisher that sends insults from INSULT list
# to a pubsubchannel

import redis
import time

# Connect to Redis
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

channel_name = "insult_channel"

# Publish multiple messages
messages = [
    "Eres más lento que un for en Python sin optimizar.",
    "Tienes más bugs que un código sin tests.",
    "Eres como un try sin except.",
    "Más inútil que un import que no se usa.",
    "Tienes más errores que un indent mal puesto.",
    "Eres un while True sin break.",
    "Más confuso que un lambda mal escrito.",
    "Eres como Python 2 en 2026.",
    "Tienes más paréntesis que un código mal formateado.",
    "Más perdido que un None sin validar.",
    "Eres un print en producción.",
    "Más innecesario que un pass dentro de pass.",
    "Tienes más warnings que un pip install viejo.",
    "Eres como un dict sin claves.",
    "Más inútil que un comentario TODO olvidado."
]

for message in messages:
    client.publish(channel_name, message)
    print(f"Published: {message}")
    time.sleep(2)  # Simulating delay between messages
