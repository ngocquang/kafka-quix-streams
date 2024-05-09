from quixstreams import Application, State


def consumer_input():
    print("\tConsumer start:")

    # Define an application
    app = Application(
        broker_address="localhost:29092",  # Kafka broker address
        consumer_group="consumer-group-name",  # Kafka consumer group
        auto_offset_reset="earliest",
    )

    # Define the input and output topics. By default, "json" serialization will be used
    input_topic = app.topic("my_input_topic", value_deserializer="json")
    output_topic = app.topic("my_output_topic", value_deserializer="json")

    # Create a StreamingDataFrame instance
    # StreamingDataFrame is a primary interface to define the message processing pipeline
    sdf = app.dataframe(topic=input_topic)

    # Print the incoming messages
    sdf = sdf.update(lambda value: print('Received a message:', value))

    # Select fields from incoming messages
    sdf = sdf[["field_1", "field_2", "field_3"]]

    # Filter only messages with "field_1" > 10 and "field_2" != "test"
    sdf = sdf[(sdf["field_1"] > 10) & (sdf["field_2"] != "test")]

    # Filter messages using custom functions
    sdf = sdf[sdf.apply(lambda value: 0 < (value['field_1'] + value['field_3']) < 1000)]

    # Generate a new value based on the current one
    # sdf = sdf.apply(lambda value: {**value, 'new_field': 'new_value'})

    # Update a value based on the entire message content
    sdf['field_4'] = sdf.apply(lambda value: value['field_1'] + value['field_3'])

    # Use a stateful function to persist data to the state store and update the value in place
    sdf = sdf.update(count, stateful=True)

    # Print the result before producing it
    sdf = sdf.update(lambda value: print('Producing a message:', value))

    # Produce the result to the output topic
    sdf = sdf.to_topic(output_topic)

    app.run(sdf)

    print("\tConsumer end")



def count(data: dict, state: State):
    # Get a value from state for the current Kafka message key
    total = state.get('total', default=0)
    total += 1
    # Set a value back to the state
    state.set('total', total)
    # Update your message data with a value from the state
    data['total'] = total
