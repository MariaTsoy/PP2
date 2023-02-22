import json

with open('sample-data.json') as user_file:
    file = user_file.read()

pyFile = json.loads(file)

dn = []
descr = []
speed = []
mtu = []

for i in pyFile["imdata"]:
    innerDict1 = i["l1PhysIf"]
    innerDict2 = innerDict1["attributes"]
    dn.append(innerDict2["dn"])
    descr.append(innerDict2["descr"])
    speed.append(innerDict2["speed"])
    mtu.append(innerDict2["mtu"])

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for i in range(3):
    print(dn[i], "        ", descr[i], "                  ", speed[i], " ", mtu[i])
