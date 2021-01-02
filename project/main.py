#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
---------------------------------------------
# WooCommerce Python API
# (C) 2021 Yuya Tinnefeld, Düsseldorf, Germany
# email: yuyatinnefeld@gmail.com
---------------------------------------------
"""

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