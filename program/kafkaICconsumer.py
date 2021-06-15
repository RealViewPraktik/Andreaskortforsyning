from kafka import KafkaConsumer
import json
import sys
import imagecutfacade as ICF



bootstrap_servers = ['localhost:9092']
topicName = 'locations'
consumer = KafkaConsumer (topicName, group_id = 'group1',value_deserializer=lambda m: json.loads(m.decode('utf-8')),bootstrap_servers = bootstrap_servers,auto_offset_reset = 'earliest')







try:
    for message in consumer:
        x = message.value
        print(x)
        location = x['location']
        email = x['email']
        print(x)
        ICF.get_requested_images(location, email)
except KeyboardInterrupt:
    sys.exit()
except:
    print('Something bad happend in consumer')
