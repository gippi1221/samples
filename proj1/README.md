1) launch docker-compose up -d
2) create a topic
docker-compose exec kafka kafka-topics.sh --create --topic topic_1 --partitions 1 --replication-factor 1 --bootstrap-server kafka:9092
3) validate
docker-compose exec kafka kafka-console-consumer.sh --topic topic_1 --from-beginning --bootstrap-server kafka:9092
docker-compose exec kafka kafka-console-producer.sh --topic topic_1 --broker-list kafka:9092

4) python3 -m venv venv
5) source venv/bin/activate


docker-compose run producer python ./producer.py
docker-compose run warmer python ./warmer.py

zadd top 6 test1
zadd top 2 test2
zadd top 2 test3
zadd top 3 test4
zadd top 9 test5
zadd top 7 test6
zadd top 3 test7
zadd top 4 test8
zadd top 2 test9
zadd top 1 test10

ZRANGE top 0 -1 REV


ZREMRANGEBYRANK top 0 -6


db.jokes.aggregate([{$sort: {rating: -1}}, {$limit: 5}])