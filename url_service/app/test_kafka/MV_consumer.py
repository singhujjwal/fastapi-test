from pykafka import KafkaClient
client = KafkaClient(hosts="127.0.0.1:9093")

# def get_messages(topicname):
#     def events():
#         for message in client.topics[topicname].get_simple_consumer():
#             print ("{} -> {}".format(message.offset, message.value))
#             yield f"i.value.decode()"
            
#     return events()


consumer = client.topics['geostream'].get_simple_consumer()
for message in consumer:
    print ("{} -> {}".format(message.offset, message.value))
# for x in get_messages("geostream"):
#     print(x)