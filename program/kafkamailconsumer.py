from kafka import KafkaConsumer
import json
import sys
import mailservice as ms

bootstrap_servers = ['localhost:9092']
topicName = 'ordres'
consumer = KafkaConsumer (topicName, group_id = 'group1',value_deserializer=lambda m: json.loads(m.decode('utf-8')),bootstrap_servers = bootstrap_servers,auto_offset_reset = 'earliest')

try:
    for message in consumer:
        x = message.value
        
        orderid = x['orderID']
        mail = x['mail']
        print(orderid, mail)
        ms.mail_sender(orderid, mail)        
except KeyboardInterrupt:
    sys.exit()
