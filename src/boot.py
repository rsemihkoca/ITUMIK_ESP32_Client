# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
from wifi import WiFiManager
import os

# Wi-Fi credentials
wifi_ssid = "your_wifi_ssid"
wifi_password = "your_wifi_password"



# Instantiate the WiFiManager and MQTTSubscriber classes
wifi_manager = WiFiManager(wifi_ssid, wifi_password)

# Connect to Wi-Fi, MQTT, run, and disconnect
wifi_manager.connect()

# Check if the original main.py exists
if 'main.py.orig' in os.listdir():
    # Rename main.py.orig back to main.py
    os.rename('main.py.orig', 'main.py')

# Check if main.py exists
if 'main.py' in os.listdir():
    # Run main.py
    exec(open('main.py').read())

