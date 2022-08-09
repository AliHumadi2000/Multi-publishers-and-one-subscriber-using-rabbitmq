import pika
from pika.exchange_type import ExchangeType
# create connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()
# declare the name of the queue
channel.exchange_declare(exchange='multi', exchange_type=ExchangeType.fanout)
# declare the name of the queue

message = 'hello world! from publisher 3'
channel.basic_publish(exchange='multi', routing_key='', body=message)
print("[x] Sent...", message)
connection.close()
