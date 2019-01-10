import paho.mqtt.client as mqtt
import smsgateway
import fbfunction
import datetime
username = "ragil"
password = "ragil"
topic = "lab/#"
server = "192.168.100.58"
client = mqtt.Client("client")
number = ['082220488112','089657219404']
cldr = 30
cpir = 30
carus = 30
csuhu = 30
csmoke = 30

# fbfunction.post('arus',str(datetime.datetime.now()),'entah')
def on_connect(client, userdata, rc):
    print ("connected" + str(rc))
    client.subscribe(topic)
def on_message(client, userdata, msg):
    if(str(msg.topic)=="lab/ldr/s1"):
        print("ldr")
        print("Message :" + str(msg.payload.decode("utf-8")))
        print(str(datetime.datetime.now()))
        print(type(cpir))
        print(cldr)
        print(csmoke)
        print(csuhu)
        fbfunction.post('arus',str(datetime.datetime.now()),str(value))
        value = int(str(msg.payload.decode("utf-8")))
        if cldr > 29:
            fbfunction.post('light',str(datetime.datetime.now()),str(value))
            cldr = 0
        cldr += 1
    if(str(msg.topic)=="lab/temperature/s1"):
        print("temperature")
        print("Message :" + str(msg.payload.decode("utf-8")))
        value = int(str(msg.payload.decode("utf-8")))
        print (value)
        fbfunction.post('temperature',str(datetime.datetime.now()),str(value))
        smsgateway.kirim_pesan('082220488112',"temperature "+ str(value))
        
        if (value > 35 or csuhu > 29):
            for i in number:
                  smsgateway.kirim_pesan(i,"temperature "+ str(value))
                  fbfunction.post('temperature',str(datetime.datetime.now()),str(value))
            csuhu = 0
        csuhu += 1
    if(str(msg.topic)=="lab/current/s1"):
        print("current")
        print("Message :" + str(msg.payload.decode("utf-8")))
        value = int(str(msg.payload.decode("utf-8")))
        if carus > 29:
            fbfunction.post('arus',str(datetime.datetime.now()),str(value))
            carus = 0
        carus += 1
    if(str(msg.topic)=="lab/pir/s1"):
        print("pir")
        print("Message :" + str(msg.payload.decode("utf-8")))
        value = int(str(msg.payload.decode("utf-8")))
        if cpir > 29:
            fbfunction.post('motion',str(datetime.datetime.now()),str(value))
            cpir = 0
        cpir += 1
    if(str(msg.topic)=="lab/smoke/s1"):
        print("smoke")
        print("Message :" + str(msg.payload.decode("utf-8")))
        value = int(str(msg.payload.decode("utf-8")))
        if (value > 900 or csmoke > 29):
              for i in number:
                    smsgateway.kirim_pesan(i,"temperature "+ str(value))
              fbfunction.post('asap',str(datetime.datetime.now()),str(value))
              csmoke = 0
        csmoke += 1

client.on_message = on_message
client.username_pw_set('ragil','ragil')
client.connect(server)
client.subscribe(topic)
client.loop_forever()
client.disconnect()
