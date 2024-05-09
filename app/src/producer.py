from quixstreams import Application


def producer():

    print("\tProducer start:")

    app = Application(
        broker_address='localhost:29092'
    )

    # Define a topic "my_input_topic" with JSON serialization
    topic = app.topic(name='my_input_topic', value_serializer='json')

    events = [
      {"id": "1", "field_1": 20, "field_2": "Lorem field_2", "field_3": 500},
      {"id": "2", "field_1": 10, "field_2": "Lorem field_2", "field_3": 100},
      {"id": "3", "field_1": 60, "field_2": "Lorem field_2", "field_3": 500},
    ]

    # Create a Producer instance
    with app.get_producer() as producer:
        for event in events:
          # Serialize an event using the defined Topic
          kafka_msg = topic.serialize(key=event["id"], value=event)

          # Produce a message into the Kafka topic
          producer.produce(
              topic=topic.name, value=kafka_msg.value, key=kafka_msg.key
          )
          print(f'Produce event with key="{kafka_msg.key}" value="{kafka_msg.value}"')

    print("\tProducer end")
    return
