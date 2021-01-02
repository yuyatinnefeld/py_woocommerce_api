from conf import WooCommerce
from woocommerce import API
import json

class WCAPI():

    def setup(self):
        wc = WooCommerce()
        key = wc.get_key()
        secret = wc.get_secret()

        wcapi = API(
            url='http://wanamour.de/',
            consumer_key = key,
            consumer_secret = secret,
            version="wc/v3"
        )

        print("🐍 api setup done 🐍")
        return wcapi


    def extract_to_json(self, query, wcapi, data_path):
        data = wcapi.get(query)
        json_data = data.json()
    
        with open(data_path, 'w') as f:
            json.dump(json_data, f)
        
        print("🐍 data extracted 🐍")
