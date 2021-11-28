import httplib, json, urllib
import urllib2

def thingspeak_get():
    api_key_read = "6YNXJ1USFIYOOLI3"
    channel_ID = "1587079"
    TS = urllib2.urlopen("https://api.thingspeak.com/channels/%s/fields/1/last.json?api_key=%s" % (channel_ID, api_key_read))
    response = TS.read()
    data=json.loads(response)
    TS.close()
    value = data['field1']
    return value

value = thingspeak_get( )
print(value)