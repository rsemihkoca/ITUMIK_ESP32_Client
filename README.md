# ITUMIK_ESP32_Client
* The data received from the distance sensors is processed and sent to the HiveMQ broker. 
* Can establish a MongoDB connection (coming soon)
* Added semi-OTA support with ugit:(coming soon)
* On every reboot the source code is retrieved from the github repository (coming soon)
* The secret information required to connect to the broker is pulled from mongodb from device-specific documentation. (To be added)

In the near future I will also add a remote reboot feature to be fully remote OTA. This way it will update the source code itself when rebooted remotely. Necessary credentials will come from mongodb. We can think of it like this. There is a function (github) there are parameters required for the function (secrets). When both of these are remote, it will be fully open to remote development. (To be added)

The reason for doing it this way is to reduce the setup cost as the number of clients will increase. To complete a fully automated CI/CD chain.

get_copy.py uses ampy and --port /dev/ttyUSB0 to copy all files and folders in ESP32 to the directory it resides in.
***Caution: If you want to edit the code, make sure you don't make the root directory ("/") your own computer. Otherwise you will overwrite the "lib" folder in ESP32 to "lib" in your root directory.

HiveMQ Cloud Broker Credentials Generation for ESP32
https://colab.research.google.com/drive/1FQKwWunu_sDNsPV7wvlnp-U9CZSh2kyD#scrollTo=BUH75bq5CHu5


ampy -p /dev/ttyUSB0 put cloud-mongodb-com.der /cert/cloud-mongodb-com.der

Prerequisities:
lib/mip library(package manager) or if we need additional packages for future cases
lib/ugit(repo clone)
cert/mongodb_cert.der
cert/hivemq_cert.der
