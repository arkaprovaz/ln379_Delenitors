import paho.mqtt.client as mqtt
import time
import json
from CRUD import pushToDB


mqtt_config = "jsons/mqtt_config.json"

with open(mqtt_config, 'r') as openfile:
    config = json.load(openfile)

mqtt_sub_topic = config["topic"]
client = mqtt.Client()


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
    print(a)
    pushToDB(a)


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
