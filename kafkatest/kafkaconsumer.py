from kafka import KafkaConsumer
import sys
import x

bootstrap_servers = ['localhost:9092']
topicName = 'ordres'
consumer = KafkaConsumer (topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers,
auto_offset_reset = 'earliest')




try:
    for message in consumer:
        x.afunction(message.value)
        #print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
except KeyboardInterrupt:
    sys.exit()
