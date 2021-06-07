from kafka import KafkaProducer
import DBfacade as DBF
import json

bootstrap_servers = ['localhost:9092']
topicName = 'ordres'
producer = KafkaProducer(bootstrap_servers='localhost:9092')

def send_order(orderid, email):
    producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
    producer.send('ordres', {'orderID': orderid, 'mail': email})


