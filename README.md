# WooCommerce API Revenue Dashboard

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
json_data_location = 'data/orders.json'

orders_data = orders.json()
with open(json_data_location, 'w') as f:
    json.dump(orders_data, f)
```

8. transform the Json data with pandas

```bash
pip install pip install pandas
```

9. create data_prep.py

```python
import pandas as pd 

class Processer():
    def preparation(self, json_data):
        df_orders = pd.read_json (json_data)
        num_orders = df_orders.shape[0]
        data = []

        for i in range(0, num_orders):
            products = df_orders.iloc[i].line_items

            for p in products:
                order_id = df_orders.iloc[i].id
                date = df_orders.iloc[i].date_created
                payment = df_orders.iloc[i].payment_method
                sku = p.get('sku')
                
                if(p.get('parent_name')):
                    name = p.get('parent_name')
                    variant = p.get('meta_data')[0].get('value')

                else:
                    name = p.get('name')
                    variant = ""

                price = p.get('price')
                quantity = p.get('quantity')
                
                d = {'order_id': order_id, 'date': date, 'payment':payment, 'sku':sku, 'product name':name, 'variant':variant, 'price': price, 'quantity':quantity}
                data.append(d)
        
        df_result = pd.DataFrame(data, columns = ['date', 'payment','sku', 'product name','variant','price', 'quantity'])
        df_result.to_csv('data/result.csv', encoding='utf-8')
```

10. import this data_prep in the app.py and use the Processer

```python
from data_prep import Processer

....

processer =  Processer()
processer.preparation(json_data_location)
```


