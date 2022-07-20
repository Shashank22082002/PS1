import pika
import json

params = pika.URLParameters(
    'amqps://ihmjanpu:4XqHoydYlSJeU-tvf0M_HjDgN98uqG17@puffin.rmq2.cloudamqp.com/ihmjanpu')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def callback(ch, method, properties, body):
    answer = json.loads(body)
    print(f'Received answer: {answer} \n')
    with open('answer.txt', 'w') as f:
        f.write(answer)


channel.basic_consume(
    queue='answer', on_message_callback=callback, auto_ack=True)

print('Started Consuming Answer')

channel.start_consuming()

channel.close()
