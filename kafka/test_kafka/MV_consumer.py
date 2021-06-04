from pykafka import KafkaClient
client = KafkaClient(hosts="127.0.0.1:9093")
# for x in get_messages("geostream"):
#     print(x)

consumer = client.topics['geostream'].get_simple_consumer()
for message in consumer:
    if message is not None:
        print (" {} -> {}".format(message.offset, message.value))