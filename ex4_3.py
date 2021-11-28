import httplib, json, urllib
from time import sleep
from random import randint

def make_param_thingspeak(data):
    params = urllib.urlencode({'field1': data})
    return params

def thingspeak_post(params):
    api_key_write = "G7JD0XZ14OD7HFXR"
    headers = {"Content-type": "application/x-www-form-urlencoded","X-THINGSPEAKAPIKEY":api_key_write}
    conn = httplib.HTTPSConnection("api.thingspeak.com")
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    respone_data = response.read()
    conn.close()    
    return respone_data

while True:
    data_random = randint(0,50)
    print(data_random)
    
    params_thingspeak = make_param_thingspeak(data_random)
    thingspeak_post(params_thingspeak)
    
    sleep(3)
