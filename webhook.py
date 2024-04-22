import requests
import json

link = 'https://sms-api-pointer.pontaltech.com.br/v1'
webhook_url = 'http://127.0.0.1:5000/send_sms'

sms = {
    "from": "5511999999999",
    "text": "Lorem ipsum lorem ipsum",
    "to": 5511988888888,
    "id": 99999,
    "token": "aqddadsddfdd74489745777aakdsajkdd"
}

sms_json = json.dumps(sms)
requests.post(webhook_url, data=sms_json)