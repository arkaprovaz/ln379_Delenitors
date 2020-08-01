import paho.mqtt.client as mqtt
import time
import random
import json
from datetime import datetime

mqtt_config = "mqtt_config.json"

with open(mqtt_config, 'r') as openfile: 
    config = json.load(openfile) 

   

mqtt_pub_topic = config["topic"]
client=mqtt.Client()

def on_connect(client, userdata, flags, rc):
    client.connected_flag=True
    client.disconnect_flag=False
    print("Connected")
    print("rc: " + str(rc))

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

def on_disconnect(client, userdata, rc):
    print("disconnecting reason  "  +str(rc))
    client.connected_flag=False
    client.disconnect_flag=True
    client.loop_stop()

def on_message(client, userdata, message):
    message_received=json.loads(message.payload)
    print("message received  ",message_received)

def init_mqtt(client,mqtt_host,mqtt_port,mqtt_uid,mqtt_password):
    mqtt.Client.connected_flag=False
    client.username_pw_set(username=mqtt_uid,password=mqtt_password)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect    
    client.on_publish = on_publish
    client.connect(mqtt_host, int(mqtt_port))
    #client.subscribe(mqtt_topic)
    client.loop_start()
    while not client.connected_flag: #wait in loop
        print("In wait loop")
        time.sleep(1)
    #return 0

def handler():
    mqtt_host = config["mqtt_host"]
    mqtt_port = config["mqtt_port"]
    mqtt_uid = config["mqtt_uid"]
    mqtt_password = config["mqtt_password"]
    #Connection initiated

    init_mqtt(client,mqtt_host,mqtt_port,mqtt_uid,mqtt_password)
    while client.connected_flag:
        config_data = {
            "DID" : "LORA_NODE_1" ,
            "rf" : round(random.uniform(0.0,200.0),2),
            "wl" : round(random.uniform(50.0,300.0),3),
            "temp" : round(random.uniform(20.0,45.0),2),
            "humid" : round(random.uniform(20.0,100.0),2),
            "ws" : round((random.random()*100),2),
            "press" : round((random.random()*100),2),
            "wd" : "NE"
            
        }
        client.publish(str(mqtt_pub_topic),str(config_data))
        print(config_data)
        time.sleep(5)
        
if __name__ == "__main__": 
    handler()
