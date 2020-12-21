from conf import WooCommerce
from woocommerce import API
import json

wc = WooCommerce()
key = wc.get_key()
secret = wc.get_secret()


wcapi = API(
    url='http://wanamour.de/',
    consumer_key = key,
    consumer_secret = secret,
    version="wc/v3"
)

#print("### TEST START ###")
#r = wcapi.get("products")
#print(r)
#print(r.status_code)
#print(r.headers['content-type'])
#print(r.encoding)
#print(r.text)
#print(r.json())
#print("### TEST END ###")

orders = wcapi.get("orders")
orders_data = orders.json()
with open('orders.json', 'w') as f:
    json.dump(orders_data, f)


#customers = wcapi.get("customers")
#customers_data = customers.json()
#with open('customers.json', 'w') as f:
#    json.dump(customers_data, f)


#products = wcapi.get("products")
#product_data = products.json()
#with open('result.json', 'w') as f:
 #   json.dump(product_data, f)

