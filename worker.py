import pika

print('Connection to RabbitMQ...')

# establishing a connection
params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='worker_queue')

print('... Completed!')

def callback(ch, method, properties, body):
    print(f"Received: {body}")

channel.basic_consume('worker_queue', callback, auto_ack=True)
channel.start_consuming()