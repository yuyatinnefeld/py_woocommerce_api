from conf import WooCommerce
from woocommerce import API
import json
from data_prep import Processer

wc = WooCommerce()
key = wc.get_key()
secret = wc.get_secret()


#wcapi = API(
#    url='http://wanamour.de/',
#    consumer_key = key,
#    consumer_secret = secret,
#    version="wc/v3"
#)

json_data_location = 'data/orders.json'

#orders = wcapi.get("orders")
#orders_data = orders.json()
#with open(json_data_location, 'w') as f:
#    json.dump(orders_data, f)

processer =  Processer()
processer.preparation(json_data_location)

