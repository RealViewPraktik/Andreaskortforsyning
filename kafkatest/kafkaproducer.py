#!/usr/bin/env python
from kafka import KafkaProducer

bootstrap_servers = ['localhost:9092']
topicName = 'ordres'
producer = KafkaProducer(bootstrap_servers='localhost:9092')






ack = producer.send(topicName, b'Hello World!!!!!!!!')
metadata = ack.get()
print(metadata.topic)
print(metadata.partition)
