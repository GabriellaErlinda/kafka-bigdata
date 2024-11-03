from kafka import KafkaProducer
import json
import random
import time

# Inisialisasi producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

sensor_ids = ['S1', 'S2', 'S3']

while True:
    # Simulasikan data suhu
    sensor_id = random.choice(sensor_ids)
    suhu = random.randint(70, 100)  # Suhu antara 70°C hingga 100°C
    data = {'sensor_id': sensor_id, 'suhu': suhu}
    
    # Kirim data ke topik
    producer.send('sensor-suhu', value=data)
    print(f'Kirim: {data}')
    
    time.sleep(1)  # Kirim data setiap detik
