from kafka import KafkaProducer
import DBfacade as DBF
import json
#from bson import json_util

bootstrap_servers = ['localhost:9092']
topicName = 'locations'
producer = KafkaProducer(bootstrap_servers='localhost:9092')



def send_locations(location, email):
    producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
    id = producer.send(topicName, {'location': location, 'email': email})
    return id


location = [711544, 6175343]
email = 'test@test.com'


send_locations(location, email)



