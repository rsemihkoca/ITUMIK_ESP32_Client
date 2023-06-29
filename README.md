# ITUMIK_ESP32_Client
* The data received from the distance sensors is processed and sent to the HiveMQ broker. 
* Added semi-OTA support with ugit:(coming soon)
* On every reboot the source code is retrieved from the github repository (coming soon)

In the near future I will also add a remote reboot feature to be fully remote OTA. This way it will update the source code itself when rebooted remotely. 
The reason for doing it this way is to reduce the setup cost as the number of clients will increase. To complete a fully automated CI/CD chain.

get_copy.py uses ampy and --port /dev/ttyUSB0 to copy all files and folders in ESP32 to the directory it resides in.
***Caution: If you want to edit the code, make sure you don't make the root directory ("/") your own computer. Otherwise you will overwrite the "lib" folder in ESP32 to "lib" in your root directory.

HiveMQ Cloud Broker Credentials Generation for ESP32
https://colab.research.google.com/drive/1FQKwWunu_sDNsPV7wvlnp-U9CZSh2kyD#scrollTo=BUH75bq5CHu5


ampy -p /dev/ttyUSB0 put cloud-mongodb-com.der /cert/cloud-mongodb-com.der

Prerequisities:
cert/hivemq_cert.der
