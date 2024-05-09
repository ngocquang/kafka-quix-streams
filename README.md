# Kafka with Quix Streams

This Repo provides instructions on how to set up and use Kafka with
Quix Streams.

## Start Kafka

```bash
docker-compose up -d
nc -zv localhost 22181
```

## Setup Quix Stream

```bash
# Onetime
python3 -m venv myenv
source myenv/bin/activate # MacOS
# myenv\Scripts\activate.bat # Windows
pip3 install -r requirements.txt

```

## Producer Consumer

```bash
# Start consumer_input (in new terminal)
python3 app/main.py --action=consumer_input

# Start consumer_output (in new terminal)
python3 app/main.py --action=consumer_output

# Start producer (in new terminal)
python3 app/main.py --action=producer


# Looking result in consumer_output

```

## Kafka CLI (Advanced)

```bash
# Create topic
docker exec kafka kafka-topics --bootstrap-server kafka:9092 \
--create --topic my_topic_1 --partitions 1 --replication-factor 1
docker exec kafka kafka-topics --bootstrap-server kafka:9092 \
--create --topic my_input_topic --partitions 1 --replication-factor 1
docker exec kafka kafka-topics --bootstrap-server kafka:9092 \
--create --topic my_output_topic --partitions 1 --replication-factor 1

# List topics
docker exec kafka kafka-topics --bootstrap-server kafka:9092 \
--list

# Describe topic
docker exec kafka kafka-topics --bootstrap-server kafka:9092 \
--describe --topic my_topic_1

# Produce message
docker exec kafka \
bash -c "echo 'Hello World!' | kafka-console-producer --request-required-acks 1 --broker-list kafka:9092 --topic my_topic_1"

docker exec kafka \
bash -c "seq 42 | kafka-console-producer --request-required-acks 1 --broker-list kafka:9092 --topic my_topic_1 && echo 'Produced 42 messages.'"


# Consume message
docker exec kafka \
kafka-console-consumer --bootstrap-server kafka:9092 --topic my_topic_1 --group my-first-application

docker exec kafka \
kafka-console-consumer --bootstrap-server kafka:9092 --topic my_input_topic --group my-first-application

# Unless specifying the --from-beginning option, only future messages will be displayed and read.
docker exec kafka \
kafka-console-consumer --bootstrap-server kafka:9092 --topic my_topic_1 --from-beginning --max-messages 42 --group my-first-application
```
