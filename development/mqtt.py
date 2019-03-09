import paho.mqtt.client as mqtt
import smsgateway
import function
import datetime
from datetime import timedelta
username = "ragil"
password = "ragil"
topic = "lab/#"
server = "192.168.100.58"
client = mqtt.Client("client-fbclient")
client.username_pw_set(username,password)
tTemperature = datetime.datetime.now()
tSmoke = datetime.datetime.now()
tDefault = datetime.datetime.now()
tDefault1 = datetime.datetime.now()
tDefault2 = datetime.datetime.now()
tNotif = datetime.datetime.now()
delayUpdate = timedelta(minutes=10)
delayNotif = timedelta(minutes=1)
print("Running at")
print(str(datetime.datetime.now()))

def on_connect(client, userdata, rc):
        print ("connected" + str(rc))
def on_message(client, userdata, msg):
        # print("Topic :" + str(msg.topic))
        global tDefault,tDefault1,tDefault2,tTemperature,tSmoke,tNotif
        # print("Message :" + str(msg.payload.decode("utf-8")))
        # print ("client"+str(datetime.datetime.now()))
        if(str(msg.topic)=="lab/pir"):
                
                if (msg.payload.decode("utf-8")=="0"):
                        value = "Tidak ada Aktifitas"
                elif (msg.payload.decode("utf-8")=="1"):
                        value = "Terdapat Aktifitas"
                else:
                        value = "Not Defined"
                if ((datetime.datetime.now()-tDefault)>=delayUpdate) :
                        function.post("pir",value)
                        tDefault = datetime.datetime.now()
                        
                # function.put("pir",value)

        if(str(msg.topic)=="lab/temperature"):
                value = str(msg.payload.decode("utf-8"))
                if ((datetime.datetime.now()-tTemperature)>=delayUpdate or int(value)>30) :
                        if int(value)>30:
                                function.post("temperature",value)
                                tTemperature = datetime.datetime.now()
                                function.notif("Suhu tidak wajar "+ str(value) +" derajat Celcius")
                        else:
                                function.post("temperature",value)
                                tTemperature = datetime.datetime.now()
                

        if(str(msg.topic)=="lab/smoke"):
        #         # smsgateway.kirim_pesan("082220488112","Tingkat Asap: " + str(msg.payload.decode("utf-8")))
        #         # function.post("smoke",str(msg.payload.decode("utf-8")))
        #         # function.put("smoke",str(msg.payload.decode("utf-8")))
                value = str(msg.payload.decode("utf-8"))
                if ((datetime.datetime.now()-tSmoke)>=delayUpdate or int(value)>204) :
                        if int(value)>204:
                                function.post("smoke",value)
                                tSmoke = datetime.datetime.now()
                                function.notif("Asap berbahaya")
                                function.pesan("082220488112","Tingkat Asap Berbahaya!!")
                        else:
                                function.post("smoke",value)
                                tSmoke = datetime.datetime.now()
                        
                

        if(str(msg.topic)=="lab/current"):
                value = str(msg.payload.decode("utf-8"))
                if ((datetime.datetime.now()-tDefault1)>=delayUpdate) :
                        function.post("current",value)
                        tDefault1 = datetime.datetime.now()

        if(str(msg.topic)=="lab/ldr"):
        #         print(type(msg.payload.decode("utf-8")))
                ldr = int(msg.payload.decode("utf-8"))
                if (ldr > 758):
                        value = "Hidup"
                elif (ldr > 0 and ldr < 300):
                        value = "Mati"
                if ((datetime.datetime.now()-tDefault2)>=delayUpdate):
                        function.post("ldr",value)
                        tDefault2 = datetime.datetime.now()
                        
                

        # if(str(msg.topic)=="lab/ldr"):
        #         value = "Not Defined"
        #         if (msg.payload.decode("utf-8")>800):
        #                 value = "Sangat Terang"
        #         elif (msg.payload.decode("utf-8")<800 and msg.payload.decode("utf-8") > 300):
        #                 value = "Normal"
        #         elif (msg.payload.decode("utf-8")>0 and msg.payload.decode("utf-8")<300):
        #                 value = "Redup"
        #         function.put("ldr","tes")


client.on_message = on_message
client.connect(server)
client.subscribe(topic)
client.loop_forever()
client.disconnect()