import json

# some JSON:
x =  '{"channel_id":1587079,"created_at":"2021-12-11T05:35:31Z","entry_id":797,"field1":null,"field2":"21","field3":null,"field4":null,"field5":null,"field6":null,"field7":null,"field8":null,"latitude":null,"longitude":null,"elevation":null,"status":null}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["field2"])