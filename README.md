#WooCommerce API Revenue Dashboard

## Goal
For my online store I create a revenue reporting manually every month. I started with this project in order to save my time and to test my python API skills.

## Info
WooCommerce REST API SETUP:
https://docs.woocommerce.com/document/woocommerce-rest-api/

WooCommerce REST API INFO:
https://woocommerce.github.io/woocommerce-rest-api-docs/?python#create-an-order-note

## Setup

0. activate venv
```bash
python -m venv env
source env/bin/activate (Mac) or env\Scripts\activate (Windows)
```

1. install the package
```bash
pip install pip install woocommerce
```

2. create WooCommerce API and copy the consumer key and secret ID.

https://docs.woocommerce.com/document/woocommerce-rest-api/


3. paste these info in the conf.py

```python
class WooCommerce():
  def __init__(self):
    self.cunsumer_key = 'ck_xxxxxxxxx'
    self.consumer_secret = 'cs_xxxxxxxxxx'

```

4. import package in the app.py 

```python
from conf import WooCommerce
from woocommerce import API
import json
```


5. setup the WC API
```python
wc = WooCommerce()
key = wc.get_key()
secret = wc.get_secret()


wcapi = API(
    url='http://wanamour.de/',
    consumer_key = key,
    consumer_secret = secret,
    version="wc/v3"
)
```

6. get the orders info

```python
orders = wcapi.get("orders")
```

you can get other info for your own business needs
Details: http://woocommerce.github.io/woocommerce-rest-api-docs/

7. save the info as Json

```python
orders_data = orders.json()
with open('orders.json', 'w') as f:
    json.dump(orders_data, f)
```