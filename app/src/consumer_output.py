from quixstreams import Application, State


def consumer_output():
    print("\tConsumer start:")

    # Define an application
    app = Application(
        broker_address="localhost:29092",  # Kafka broker address
        consumer_group="consumer-group-name",  # Kafka consumer group
        auto_offset_reset="earliest",
    )

    # Define the input and output topics. By default, "json" serialization will be used
    input_topic = app.topic("my_output_topic", value_deserializer="json")

    # Create a StreamingDataFrame instance
    # StreamingDataFrame is a primary interface to define the message processing pipeline
    sdf = app.dataframe(topic=input_topic)

    # Print the incoming messages
    sdf = sdf.update(lambda value: print('Received a message:', value))

    app.run(sdf)

    print("\tConsumer end")
