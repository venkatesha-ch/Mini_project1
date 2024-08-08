import pika, os, logging, json
logging.basicConfig()


url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')
params = pika.URLParameters(url)
params.socket_timeout = 5


def get_weather_data():
    temp = 32.0
    humidity = 73
    wind = 10.0
    precipitation = 0
    return 'Mumbai \nHaze, Excessive Heat!.\nPrecip : {}%\nHumidity : {}%\nWind: {}km/h\nFeels like {} C'.format(precipitation, humidity, wind, temp)
    
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='datacenter') 

info = get_weather_data()
channel.basic_publish(exchange='', routing_key='datacenter', body=json.dumps(info))


print ("Information sent to server")
connection.close()
