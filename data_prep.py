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





