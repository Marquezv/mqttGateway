import paho.mqtt.client as mqtt
import requests
import json
import re

from model.client import User, SimpleUser, LoginData, LoginSucess

topic_pattern_user = re.compile('/esp8266.*/sessionid.*')
url = 'http://0.0.0.0:5000'


def on_connect(client, userdata, flags, reason_code):
    print(f"Connected with result code {reason_code}")
    
def req_login():
    r = requests.post(url+'/login', json={'name': 'Lua', 'password': '001'})
    ret = r.json()
    print(ret)

    
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
 #   req = msg.payload.json()
 #   print(req)
 #   req_login()
    
def on_publish(client, userdata, result):
    print("data published \n")
    
    
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_publish = on_publish

mqttc.connect("192.168.12.1", 1883, 60)

mqttc.subscribe("#");


mqttc.loop_forever()
