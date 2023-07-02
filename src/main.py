from mqtt import MQTTSubscriber
from hcsr04 import HCSR04
from time import sleep
from wifi import WiFiManager
import ubinascii
import machine
import network
from machine import Pin
import random
from ucollections import OrderedDict
import json

import gc
gc.collect()


# HiveMQ Cloud credentials from secrets.py
try:
    from secrets import secrets
except ImportError:
    print("Error, secrets could not be read")
    raise

# ESP32
sensor1 = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
sensor2 = HCSR04(trigger_pin=4, echo_pin=16, echo_timeout_us=10000)


print('----------------------------------------------------------------------------------------------')
print("Connecting to " + secrets["cluster_url"] + " as user " + secrets["username"])
# Instantiate the MQTTSubscriber class
subscriber = MQTTSubscriber(
    server= secrets["cluster_url"], #"broker.hivemq.com"
    port= secrets["port"],
    client_id= ubinascii.hexlify(machine.unique_id()),
    username= secrets["username"],
    password= secrets["password"],
    topic= secrets["topic"], 
    ssl= True,
    ssl_params=secrets["ssl_params"]
)

# Connect, run, and disconnect
subscriber.connect()
subscriber.subscribe()
print("Subscribed to: ", secrets["topic"])


def calculate_occupancy(distance1,distance2):

    if distance1<0 or distance2<0:
        return False
    
    elif distance1<=50 or distance2<=50:
        return True

    else:
        return False



while True:
    distance1 = sensor1.distance_cm()
    distance2 = sensor2.distance_cm()

    print('sensor x Distance:', distance1, 'cm')
    
    print('sensor y Distance:', distance2, 'cm')
    print("")
    subscriber.client.check_msg()


    message = OrderedDict()
    message["Chair001"] = calculate_occupancy(distance1, distance2)
    message["Chair002"] = calculate_occupancy(random.randint(0, 150), random.randint(0, 150))
    message["Chair003"] = calculate_occupancy(random.randint(0, 150), random.randint(0, 150))
    message["Chair004"] = calculate_occupancy(random.randint(0, 150), random.randint(0, 150))
    json_data = json.dumps(message)

    print(json_data)
    subscriber.publish(json_data)
    sleep(1)










