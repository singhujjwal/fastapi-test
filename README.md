# fastapi-test
This is directly copied from https://dev.to/paurakhsharma/microservice-in-python-using-fastapi-24cc to help me understand fastapi as well as brush up my python.
Enough of just DevOps !!!

## Now comes a demo project on top of fastapi
I have few resources available, I need to create a distributed application

## Build docker images
   `docker build -t singhujjwal/cast-service:0.1 .`
   `docker image push singhujjwal/cast-service:0.1`
   `docker run -it --rm --name cast-service -w /app singhujjwal/cast-service:0.1 uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`


   `docker build -t singhujjwal/movie-service:0.1 .`
   `docker image push singhujjwal/movie-service:0.1`

   `docker build -t singhujjwal/url-service:0.1 .`
   `docker image push singhujjwal/url-service:0.1`
   `docker run -it --rm --name urls -w /app -p 8121:8121 singhujjwal/url-service:0.1 uvicorn app.main:app --reload --host 0.0.0.0 --port 8121`
   `docker image push singhujjwal/url-service:0.1`




### Redis for cache - memcache
Update the redis service to use the clusterIP type and don't expose it as a loadbnalancer service as it doesn't need to be accessed from outside.

Also utilize the nginx ingress controller to access the redis via the port 80 
to access redis cli.

`rdcli -h civo.singhjee.in/redis -a passwd -p 80`


### Postgresql for database
### Message queue KAFKA or RabbitMQ TBD
### Python based backend dockers
### Frontend TBD vue.js or flutter

https://github.com/pedrodeoliveira/fastapi-kafka-consumer/blob/master/main.py
https://iwpnd.pw/articles/2020-03/apache-kafka-fastapi-geostream



## Helm in k3s

```
helm repo add bitnami https://charts.bitnami.com/bitnami
kubectl create ns kafka
helm install kafka --set replicaCount=3 bitnami/kafka -n kafka
```

```
NAME: kafka
LAST DEPLOYED: Wed Apr 21 22:37:51 2021
NAMESPACE: kafka
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
** Please be patient while the chart is being deployed **

Kafka can be accessed by consumers via port 9092 on the following DNS name from within your cluster:

    kafka.kafka.svc.cluster.local

Each Kafka broker can be accessed by producers via port 9092 on the following DNS name(s) from within your cluster:

    kafka-0.kafka-headless.kafka.svc.cluster.local:9092
    kafka-1.kafka-headless.kafka.svc.cluster.local:9092
    kafka-2.kafka-headless.kafka.svc.cluster.local:9092

To create a pod that you can use as a Kafka client run the following commands:

    kubectl run kafka-client --restart='Never' --image docker.io/bitnami/kafka:2.8.0-debian-10-r0 --namespace kafka --command -- sleep infinity
    kubectl exec --tty -i kafka-client --namespace kafka -- bash

    PRODUCER:
        kafka-console-producer.sh \

            --broker-list kafka-0.kafka-headless.kafka.svc.cluster.local:9092,kafka-1.kafka-headless.kafka.svc.cluster.local:9092,kafka-2.kafka-headless.kafka.svc.cluster.local:9092 \
            --topic test

    CONSUMER:
        kafka-console-consumer.sh \

            --bootstrap-server kafka.kafka.svc.cluster.local:9092 \
            --topic test \
            --from-beginning
```
