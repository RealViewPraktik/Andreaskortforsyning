from kafka import KafkaProducer



producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('orders', b'hello world')
producer.send('orders',key=b'Messge-Three', value=b'This is Kafka Python')
