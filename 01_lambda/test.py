import requests
import os
API_URL = os.environ['VITE_API_URL']
PARAMS = {
    'key1': 'value1',
    'key2': 'value2'
}

# GETリクエストを送信
response = requests.get(API_URL, params=PARAMS)
print('status code: ', response.status_code)
print('response: ', response.json())
print("--------------------------------------")