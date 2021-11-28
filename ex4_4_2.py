import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code {}".format(rc))
    channel_ID = "1587079"
    api_key_read = "6YNXJ1USFIYOOLI3"
    # client.subscribe("channels/%s/subscribe/fields/field1/%s" % (channel_ID, api_key_read))
    client.subscribe("channels/%s/subscribe/fields/field2" % (channel_ID))

def on_disconnect(client, userdata, rc):
    print("Disconnected From Broker")
    
def on_message(client, userdata, message):
    print(message.payload.decode())
    #print(message.topic)
    
client = mqtt.Client()

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
# client.username_pw_set(username = "linhtrucyeudoi", password = "WW54WCQIF5LPDGKE")
client.connect("mqtt.thingspeak.com", 1883, 60)
client.loop_forever()

