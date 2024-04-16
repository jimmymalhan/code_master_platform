import psycopg2
import json
from confluent_kafka import Producer, KafkaException

# Establishing a PostgreSQL connection
def connect_postgres():
    try:
        connection = psycopg2.connect(
            host='localhost',
            database='postgres',  # Use the default 'postgres' database
            user='jimmy',         # Username
            password='admin'      # Password
        )
        print("Database connection established")
        return connection
    except Exception as e:
        print(f"Error connecting to PostgreSQL database: {e}")

# Initializing Kafka Producer
def create_kafka_producer():
    try:
        producer = Producer({
            'bootstrap.servers': 'localhost:9092',
            'client.id': 'salesbricks-producer'
        })
        print("Kafka producer created")
        return producer
    except KafkaException as e:
        print(f"Error creating Kafka producer: {e}")
        return None

# Example function to send a message to Kafka
def send_event(producer, topic, event_data):
    if producer is not None:
        try:
            producer.produce(topic, value=event_data, callback=delivery_report)
            producer.flush()
            print(f"Event sent to {topic}")
        except Exception as e:
            print(f"Error sending event to Kafka: {e}")
    else:
        print("Producer is not initialized.")

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Main function to setup the infrastructure
def main():
    db_connection = connect_postgres()
    producer = create_kafka_producer()
    
    # Example event data
    event_data = json.dumps({'event_type': 'ORDER_CLOSED_WON', 'details': {'order_id': 123, 'total_value': 10000}})
    
    # Sending an event to Kafka
    send_event(producer, 'sellblocks_events', event_data)

    # Always close the database connection and finalize Kafka producer when done
    db_connection.close()
    if producer:
        producer.flush()  # Ensures all messages are delivered and all resources are freed.

if __name__ == '__main__':
    main()
