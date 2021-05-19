from pykafka import KafkaClient
import time

client = KafkaClient("127.0.0.1:9093")
geostream = client.topics["geostream"]



with geostream.get_sync_producer() as producer:
    i = 0
    for _ in range(10):
        producer.produce(("Kafka is not just an author " + str(i)).encode('ascii'))
        i += 1
        time.sleep(1)
        print ("Posted {}".format(i))
