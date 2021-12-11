import paho.mqtt.client as mqtt3
import json

def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code {}".format(rc))
    channel_ID = "1587079"
    api_key_read = "6YNXJ1USFIYOOLI3"
    # client.subscribe("channels/%s/subscribe/fields/field2/%s" % (channel_ID, api_key_read))
    #client.subscribe("channels/%s/subscribe/fields/field2" % (channel_ID))
    client.subscribe("channels/1587079/subscribe")

def on_disconnect(client, userdata, rc):
    print("Disconnected From Broker")
    
def on_message(client, userdata, message):
    # print(message.payload.decode())
    incoming_handling(message.payload.decode())
    #print(message.topic)



# -----------------------------------------------------------------------------------
def incoming_handling(str):
    json_object = json.loads(str)
    data2 = json_object["field2"]
    print(data2)
# -----------------------------------------------------------------------------------




client_ID="BBAABzs5KjI7JAU6GB8ZPQ8"
client = mqtt3.Client(client_id=client_ID, clean_session=True)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.username_pw_set(username = "BBAABzs5KjI7JAU6GB8ZPQ8", password = "nWE70ZAKS1+42Pl6n56SvNZP")
client.connect("mqtt3.thingspeak.com", 1883, 60)
client.loop_forever()

