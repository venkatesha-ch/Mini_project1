import pika, os, time, json, time

def process_request(msg):
  time.sleep(5)
  print("Recieved information from ", end="")
  print(json.loads(msg))
  print("----------")
  return;

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='datacenter') # Declare a queue
print("Sever started....")


# create a function which is called on incoming messages
def callback(ch, method, properties, body):
    process_request(body)

# set up subscription on the queue
channel.basic_consume('datacenter',
  callback,
  auto_ack=True)

# start consuming (blocks)
channel.start_consuming()
connection.close()
