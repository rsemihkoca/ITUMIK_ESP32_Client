import time
from umqtt.robust import MQTTClient
import ntptime
from secrets import secrets

class MQTTSubscriber:
    def __init__(self, server, port, client_id, username, password, topic, ssl, ssl_params):
        self.server = server
        self.port = port
        self.client_id = client_id
        self.username = username
        self.password = password
        self.topic = topic
        self.ssl = ssl
        self.ssl_params = ssl_params
        self.validate_cerf()
        self.client = MQTTClient(self.client_id, self.server, port=self.port, user=self.username, password=self.password, ssl=self.ssl, ssl_params=self.ssl_params)
        self.client.set_callback(self.callback)

    def callback(self, topic, msg):
        pass
        #print("Received message on topic: {}".format(topic, msg))

    def connect(self):
        self.client.connect()
        print('Connected to MQTT Broker: ' + secrets["cluster_url"])
    
    def subscribe(self):
        self.client.subscribe(self.topic)
        print('Subscribed to MQTT Broker: ' + secrets["cluster_url"])


    def publish(self, message):
        self.client.publish(self.topic, message)


    def disconnect(self):
        self.client.disconnect()
    
    def validate_cerf(self):
        
        # To validate certificates, a valid time is required
        print('----------------------------------------------------------------------------------------------')
        print('Connecting to NTP')
        ntptime.host = "de.pool.ntp.org"
        ntptime.settime()
        print('Current time: ' + str(time.localtime()))

