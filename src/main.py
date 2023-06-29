from mqtt import MQTTSubscriber
from hcsr04 import HCSR04
from time import sleep
from wifi import WiFiManager
import ubinascii
import machine
import network
from machine import Pin


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

while True:
    distance1 = sensor1.distance_cm()
    distance2 = sensor2.distance_cm()

    print('sensor x Distance:', distance1, 'cm')
    
    print('sensor y Distance:', distance2, 'cm')
    print("")
    
    
    message = dict()
    message["x distance(cm)"] = distance1
    message["y distance(cm)"] = distance2
    subscriber.client.check_msg()

    subscriber.publish(str(message))
    sleep(1)

subscriber.disconnect()

    







