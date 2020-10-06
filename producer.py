import pika

print('Connection to RabbitMQ...')

# establishing a connection
params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='worker_queue')

print('... Completed!')

i = 0
while True:
    message = str(i)
    i += 1

    channel.basic_publish(exchange='', routing_key='worker_queue', body=message)
    print(f"Message sent: {message}")

    if i > 100000:
        break

connection.close()


