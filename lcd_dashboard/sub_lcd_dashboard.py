import paho.mqtt.client as mqtt
import time
import json
from grove_rgb_lcd import *
import requests

mqtt_config = "mqtt_config.json"

with open(mqtt_config, 'r') as openfile:
    config = json.load(openfile)

mqtt_sub_topic = config["topic"]
client = mqtt.Client()
api = "http://sihvm.southcentralus.cloudapp.azure.com:5000"


def alert(level):
    if level == "EDL":
        requests.get(api + "/api/v1.0/triggerTweet")
        time.sleep(2)
        requests.get(api + "/api/v1.0/triggerEmail")
        time.sleep(2)
    if level == "DL":
        requests.get(api + "/api/v1.0/triggerTweet")
        time.sleep(2)
        requests.get(api + "/api/v1.0/triggerEmail")
        time.sleep(5)
        requests.get(api + "/api/v1.0/triggerSMS")
        time.sleep(5)
        requests.get(api + "/api/v1.0/triggerCall")
        time.sleep(2)
    else:
        time.sleep(0.01)


def on_connect(client, userdata, flags, rc):
    client.connected_flag = True
    client.disconnect_flag = False
    client.subscribe(mqtt_sub_topic)
    print("Connected")
    print("rc: " + str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " +
          str(granted_qos)+" "+"Topic: "+mqtt_sub_topic)


def on_disconnect(client, userdata, rc):
    print("disconnecting reason  " + str(rc))
    client.connected_flag = False
    client.disconnect_flag = True


def on_message(client, userdata, message):
    #print("message topic  ",str(message.topic))

    a = json.loads(message.payload.decode('utf8').replace("'", '"'))
    print("Device ID: " + "\n" + a["DID"])
    setRGB(128, 128, 128)
    setText("Device ID: " + "\n" + a["DID"])
    time.sleep(1)
    print("WLevel:" + str(a["wl"]) + "\n" + "Temp:" + str(a["temp"]))
    if a["wl"] < 10:
        setRGB(128, 0, 0)
        setText("WLevel:" + str(a["wl"]) + "\n" + "Temp:" + str(a["temp"]))
        alert("DL")
    elif a["wl"] < 15:
        setRGB(128, 0, 0)
        setText("WLevel:" + str(a["wl"]) + "\n" + "Temp:" + str(a["temp"]))
        alert("EDL")
    else:
        setRGB(0, 128, 0)
        setText("WLevel:" + str(a["wl"]) + "\n" + "Temp:" + str(a["temp"]))


def init_mqtt(client, mqtt_host, mqtt_port, mqtt_uid, mqtt_password):
    mqtt.Client.connected_flag = False
    client.username_pw_set(username=mqtt_uid, password=mqtt_password)
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.connect(mqtt_host, int(mqtt_port))


def handler():
    mqtt_host = config["mqtt_host"]
    mqtt_port = config["mqtt_port"]
    mqtt_uid = config["mqtt_uid"]
    mqtt_password = config["mqtt_password"]
    # Connection initiated
    init_mqtt(client, mqtt_host, mqtt_port, mqtt_uid, mqtt_password)
    client.loop_forever()


if __name__ == "__main__":
    handler()
