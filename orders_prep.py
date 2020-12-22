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
            print("🐍 single order in the order list added 🐍")

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






