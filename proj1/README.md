
## The system design

![alt text](./Services.svg)

### Producer:
Requests a new joke from some api service and pushes data to kafka cluster. it can be scheduled by any tools to perform this action from time to time - cron job, airflow etc..
```
docker-compose run producer python ./producer.py
```

### Kafka cluster:
Only one broker and one zookeeper are in this setup. the wurstmeister images are used.

### Consumer:
It pulls the new jokes from the kafka and stores data in the MongoDB. it also generates some rating for further ranging.

### MongoDB:
Document DB to store joke objects.

### Warmer:
The service is to update redis cache with top jkes by rating. it pulls the data from MongoDB, calculates the top-10 and refreshes data in Redis for further quering from the web. it can be scheduled by any tools to perform this action with the required interval.
```
docker-compose run warmer python ./warmer.py
```

### Redis:
It stores Sorted Set for Top-10 jokes by rating and Hashes for objects.

### Flask:
is used as a lightweight way to present data to end user. it queries data from the redis and show it by request.

## How to run it
```
docker-compose build
docker-compose up -d
```