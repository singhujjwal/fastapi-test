# URL shortener service

This microservice app will be responsible for returning the shortened url
Will try to learn few tech as part of this excerise

1. KAFKA
2. REDIS
3. CASSANDRA as well 


All pluggable module as KAFKA docker can be replaced with MSK
REDIS with Elsticcache or redis cache
CASSANDRA with DynamoDB


## Design

1. Stateless webapplicaion receives request for shorteneing a url
2. Need to send the response in synchronous mode so kafka is not a best thing here 
but I need to plugin it here any way so the webapp calls the producer to push that message to kafka first (no redis at this point)


So 

1

1. Get the message and push to the queue
2. Read from redis for 5 times and fail ---->