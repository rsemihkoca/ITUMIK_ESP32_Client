import gc
import ussl

gc.collect()

secrets = dict()



# Load certificates for HiveMQ
print('----------------------------------------------------------------------------------------------')
print('Loading CA Certificate')
# Currently only a single DER-encoded certificate is supported.(Documentation)

with open("/cert/replace_your_cert", 'rb') as f:
    cacert = f.read()
print('Obtained CA Certificate')


# Broker credentials
secrets["cluster_url"] = "your_cluster_url"
secrets["port"] = "your_port"
secrets["username"] = "your_username"
secrets["password"] = "your_password"
secrets["topic"] = b"your_topic"

# TSL credentials
ssl_params=dict()
ssl_params["server_side"] = False
ssl_params["key"] = None
ssl_params["cert"] = None
ssl_params["cadata"] = cacert
ssl_params["cert_reqs"] = ussl.CERT_REQUIRED
ssl_params["server_hostname"] = secrets["cluster_url"]

secrets["ssl_params"] = ssl_params

