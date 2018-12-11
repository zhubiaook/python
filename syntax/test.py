from kafka import KafkaConsumer, KafkaProducer


consumer = KafkaConsumer('my-topic',
                         bootstrap_servers=['192.168.0.200:9092'])

for message in consumer:
    print(f'{message.topic},'
          f'{message.partition},'
          f'{message.offset},'
          f'{message.key},'
          f'{message.value}')

producer = KafkaProducer(bootstrap_servers=['192.168.0.200:9092'])
future = producer.send('my-topic', b'raw_byte')