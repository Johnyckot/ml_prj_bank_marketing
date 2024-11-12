#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'

customer_id = 'xyz-123'

customer = {"age":27
    ,"job":"management"
    ,"marital":"single"
    ,"education":"tertiary"
    ,"default":"no"
    ,"balance":6791.0
    ,"housing":"no"
    ,"loan":"no"
    ,"contact":"telephone"
    ,"day":22
    ,"month":"mar"
    ,"duration":174.0
    ,"campaign":2
    ,"pdays":229
    ,"previous":28
    ,"poutcome":"success"
}

response = requests.post(url, json=customer).json()
print(response)

if response['subscribe_decision'] == True:
    print(f'Customer {customer_id} is likeley to subscribe')
else:
    print(f'Customer {customer_id} is NOT likeley to subscribe')