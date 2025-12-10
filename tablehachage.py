myMap={}
myMap["alice"]=88
myMap["bob"]=90

print(myMap)

myMap={"alice":80, "ouzin":50}
for key in myMap:
    print(key,myMap(key))


for val in myMap.values():
    print(val)

for key,val in myMap.items():
    print(key,val)