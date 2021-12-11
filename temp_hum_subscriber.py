import paho.mqtt.client as mqtt3
import json

def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code {}".format(rc))
    channel_ID = "1587079"
    api_key_read = "6YNXJ1USFIYOOLI3"
    client.subscribe("channels/1587079/subscribe")

def on_disconnect(client, userdata, rc):
    print("Disconnected From Broker")
    
def on_message(client, userdata, message):
    incoming_handling(message.payload.decode())
    # print(message.payload.decode())


# -----------------------------------------------------------------------------------
def incoming_handling(str):
    json_object = json.loads(str)
    temperature = json_object["field1"]
    humidity = json_object["field2"]
    print("temperature: {temp} oC\t humidity: {hum} %".format(temp = temperature, hum = humidity))
# -----------------------------------------------------------------------------------


client_ID="BBAABzs5KjI7JAU6GB8ZPQ8"
client = mqtt3.Client(client_id=client_ID, clean_session=True)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.username_pw_set(username = "BBAABzs5KjI7JAU6GB8ZPQ8", password = "nWE70ZAKS1+42Pl6n56SvNZP")
client.connect("mqtt3.thingspeak.com", 1883, 60)
client.loop_forever()