import paho.mqtt.client as mqtt3
from time import sleep
from random import randint
    
def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code {}".format(rc))
    
client = mqtt3.Client()

client.on_connect = on_connect
# client.username_pw_set(username = "linhtrucyeudoi", password = "WW54WCQIF5LPDGKE")
client.connect("mqtt.thingspeak.com", 1883, 60)


# -----------------------------------------------------------------------------------
def thingspeak_mqtt(data):
    channel_ID = "1587079"
    api_key_write = "G7JD0XZ14OD7HFXR"
    client.publish("channels/%s/publish/%s" %(channel_ID, api_key_write), "field3=%s" %(data))
# -----------------------------------------------------------------------------------


while True:
    data_random = randint(0,100)
    print(data_random)
    thingspeak_mqtt(data_random)
    sleep(3)
