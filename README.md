# fastapi-test
This is directly copied from https://dev.to/paurakhsharma/microservice-in-python-using-fastapi-24cc to help me understand fastapi as well as brush up my python.
Enough of just DevOps !!!

## Now comes a demo project on top of fastapi
I have few resources available, I need to create a distributed application

## Build docker images
   `docker build -t singhujjwal/cast-service:0.1 .`
   `docker image push singhujjwal/cast-service:0.1`


   `docker build -t singhujjwal/movie-service:0.1 .`
   `docker image push singhujjwal/movie-service:0.1`


### Redis for cache - memcache
### Postgresql for database
### Message queue KAFKA or RabbitMQ TBD
### Python based backend dockers
### Frontend TBD vue.js or flutter
