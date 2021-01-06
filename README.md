<h1 align="center">WooCommerce Python API</h1> <br>
<h2 align="center">🚀 🐍 🚀 🐍 🚀 🐍 🚀 🐍 🚀 🐍 🚀 🐍 </h2> <br>

## Table of Contents

- [About](#about)
- [Benefit](#benefit)
- [Info](#info)
- [Demo](#demo)
- [Setup](#setup)
## About
WooCommerce is an open-source e-commerce plugin for WordPress. It is designed for small to large-sized online merchants using WordPress.(Wikipedia)
## Benefit
For the creating of revenue reports manually every month takes so much time. Though the woocommerce API you can save your time and receive the automatically updated revenue reports.

## Info
WooCommerce REST API SETUP:
https://docs.woocommerce.com/document/woocommerce-rest-api/

WooCommerce REST API INFO:
https://woocommerce.github.io/woocommerce-rest-api-docs/?python#create-an-order-note

## Setup
### 0. activate venv
```bash
python -m venv env
source env/bin/activate (Mac) or env\Scripts\activate (Windows)
```

### 1. install the package
```bash
pip install pip install woocommerce
```

### 2. create the WooCommerce API and copy the consumer key and secret ID.

https://docs.woocommerce.com/document/woocommerce-rest-api/


### 3. create the wc_conf.py and paste these the key and secret

```python
class WooCommerce():
  def __init__(self):
    self.cunsumer_key = 'ck_xxxxxxxxx'
    self.consumer_secret = 'cs_xxxxxxxxxx'
    
 
  def get_key(self):
    return self.cunsumer_key

  def get_secret(self):
    return self.consumer_secret


```

### 4. create the wcapi.py for extraction & saving the WooCommerce data

```python
from wc_conf import WooCommerce
from woocommerce import API
import json

class WCAPI():

    def setup(self):
        wc = WooCommerce()
        key = wc.get_key()
        secret = wc.get_secret()

        wcapi = API(
            url='http://YOUR-WEBSITE',
            consumer_key = key,
            consumer_secret = secret,
            version="wc/v3"
        )
        print("🐍 setup done 🐍")
        return wcapi


    def extract_to_json(self, query, wcapi, data_path):
        data = wcapi.get(query)
        json_data = data.json()
    
        with open(data_path, 'w') as f:
            json.dump(json_data, f)
        
        print("🐍 data extracted 🐍")

```


### 5. create the orders_prep.py to clean & export the orders.json data 

```python
import pandas as pd 

class OrdersProcesser():

    def read(self, data_path):
        df = pd.read_json(data_path)
        print("🐍 json data loaded 🐍")
        return df

    def clean(self, df):

        def create_order_list(order_idx, product):
            
            current_order = df.iloc[order_idx]
            
            order_id = current_order.id
            date = current_order.date_created
            payment = current_order.payment_method
            
            has_variant = True if product.get('parent_name') else False
                
            name = product.get('parent_name') if has_variant else product.get('name')
            variant = product.get('meta_data')[0].get('value') if has_variant else ""
            sku = product.get('sku')
            price = product.get('price')
            quantity = product.get('quantity')
                
            d = {'order_id': order_id, 'date': date, 'payment':payment, 'sku':sku, 
                'product name':name, 'variant':variant, 'price': price, 'quantity':quantity}
            
            order_list.append(d)
            print("🐍  single order in the order list added 🐍")

        order_list, total_orders = [], df.shape[0]

        for order_idx in range(0, total_orders):
            products = df.iloc[order_idx].line_items
            
            [
                create_order_list(order_idx, product) 
                for product in products
            ]
        
        print("🐍 order list created 🐍")
        return order_list

    def export(self, data, result_data_path):
        df = pd.DataFrame(data, columns = ['date', 'payment','sku', 'product name','variant','price', 'quantity'])
        df.to_csv(result_data_path, encoding='utf-8')
        print("🐍  result as csv saved  🐍")
```

you can extract other query category (Customers, Products, Report, etc.) for your own business needs

Details: http://woocommerce.github.io/woocommerce-rest-api-docs/

### 6. create the app.py and use wcapi.py and orders_prep.py there

```python
from wcapi import WCAPI
from orders_prep import OrdersProcesser

orders_source_path, query, orders_result_path = 'data/orders.json', 'orders', 'data/orders.csv'

wcapi = WCAPI()
configuration = wcapi.setup()
wcapi.extract_to_json(query, configuration, orders_source_path)

orders_processer =  OrdersProcesser()
df = orders_processer.read(orders_source_path)
clean_orders_data = orders_processer.clean(df)
orders_processer.export(clean_orders_data, orders_result_path)
```

### 7. run the main.py and the WooCommerce data is extracted and save in the data folder.

```bash
python main.py
```

data was successfully processed if you see these messages

```bash
🐍 setup done 🐍
🐍 data extracted 🐍
🐍 json data loaded 🐍
🐍  single order in the order list added 🐍

...

🐍  single order in the order list added 🐍
🐍 order list exported 🐍
🐍  result as csv saved  🐍
```
