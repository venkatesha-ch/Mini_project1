import pika, os, logging, json
logging.basicConfig()

# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')
params = pika.URLParameters(url)
params.socket_timeout = 5

def get_weather_data():
    temp = 34.0
    humidity = 30
    wind = 10.0
    precipitation = 0
    return 'Bengaluru \nClear with periodic clouds.\nPrecip : {}%\nHumidity : {}%\nwind: {}km/h\nfeels like {} C'.format(precipitation, humidity, wind, temp)
    
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='datacenter') # Declare a queue

info = get_weather_data()
channel.basic_publish(exchange='', routing_key='datacenter', body=json.dumps(info))


print ("Information sent to server")
connection.close()
