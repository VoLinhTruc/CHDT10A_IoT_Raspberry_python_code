import Adafruit_DHT
import paho.mqtt.client as mqtt3
from time import sleep
from random import randint


channel_ID = "1587079"
api_key_write = "G7JD0XZ14OD7HFXR"


def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code {}".format(rc))

client = mqtt3.Client()
client.on_connect = on_connect

client.connect("mqtt.thingspeak.com", 1883, 60)


sensor = Adafruit_DHT.DHT11
gpio = 16

while 1:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

    if humidity is not None and temperature is not None:
        client.publish("channels/%s/publish/%s" %(channel_ID, api_key_write), "field1=%s&field2=%s" %(temperature, humidity))
        print("temperature: {temp} oC\t humidity: {hum} %".format(temp = temperature, hum = humidity))

    sleep(5)
