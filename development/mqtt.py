import paho.mqtt.client as mqtt
import smsgateway
import fcm_client
import function
import datetime
from datetime import timedelta
username = "ragil"
password = "ragil"
topic = "lab/#"
server = "192.168.100.9"
client_name = str(datetime.datetime.now())
client = mqtt.Client("client-"+client_name)
client.username_pw_set(username,password)
tTemperature = datetime.datetime.now() + timedelta(minutes=10)
tSmoke = datetime.datetime.now() - timedelta(minutes=10)
tDefault = datetime.datetime.now() - timedelta(minutes=10)
tDefault1 = datetime.datetime.now() - timedelta(minutes=10)
tDefault2 = datetime.datetime.now() - timedelta(minutes=10)
tAlertTemperature = datetime.datetime.now() - timedelta(minutes=2)
tAlertSmoke = datetime.datetime.now() - timedelta(minutes=2)
delayUpdate = timedelta(minutes=10)
delayAlert = timedelta(minutes=2)
print("Running at")
print(str(datetime.datetime.now()))

def on_connect(client, userdata, rc):
        print ("connected" + str(rc))
def on_message(client, userdata, msg):
        global tDefault,tDefault1,tDefault2,tTemperature,tSmoke, tAlertSmoke,tAlertTemperature,delayAlert
        # print("Message :" + str(msg.payload.decode("utf-8")))
        # print ("client"+str(datetime.datetime.now()))
        if(str(msg.topic)=="lab/temperatureTes"):
                value = str(msg.payload.decode("utf-8"))
                print (tAlertTemperature)

                if ((datetime.datetime.now()-tAlertTemperature)>=delayAlert and int(value) > 30) :
                        function.post("temperature",value)
                        smsgateway.kirim_pesan('082220488112','Peringatan !! Suhu berbahaya. '+value+ '° Celcius')
                        fcm_client.app_notification('Peringatan !! Suhu berbahaya. '+value+ '° Celcius\nWwaktu: '+str(datetime.datetime.now())+'')
                        tAlertTemperature = datetime.datetime.now()
        #dummy
        if(str(msg.topic)=="lab/pir"):                
                value = msg.payload.decode("utf-8")
                if ((datetime.datetime.now()-tDefault)>=delayUpdate) :
                        function.post("pir",value)
                        tDefault = datetime.datetime.now()
                        
                # function.put("pir",value)

        if(str(msg.topic)=="lab/temperature"):
                value = str(msg.payload.decode("utf-8"))
                if ((datetime.datetime.now()-tAlertTemperature)>=delayAlert and int(value) > 30) :
                        function.post("temperature",value)
                        smsgateway.kirim_pesan('082220488112','Peringatan !! Suhu berbahaya. '+value+ '° Celcius')
                        fcm_client.app_notification('Peringatan !! Suhu berbahaya. '+value+ '° Celcius\nWwaktu: '+str(datetime.datetime.now())+'')
                        tAlertTemperature = datetime.datetime.now()
                elif ((datetime.datetime.now()-tTemperature)>=delayUpdate) :
                        function.post("temperature",value)
                        tTemperature = datetime.datetime.now()
                

        if(str(msg.topic)=="lab/smoke"):
        #         # smsgateway.kirim_pesan("082220488112","Tingkat Asap: " + str(msg.payload.decode("utf-8")))
        #         # function.post("smoke",str(msg.payload.decode("utf-8")))
        #         # function.put("smoke",str(msg.payload.decode("utf-8")))
                value = str(msg.payload.decode("utf-8"))
                if ((datetime.datetime.now()-tAlertSmoke)>=delayAlert) and int(value)>403 :
                        function.post("smoke",value)
                        smsgateway.kirim_pesan("082220488112",'Tingkat asap berbahaya.')
                        fcm_client.app_notification('Waktu: '+str(datetime.datetime.now())+'Tingkat asap berbahaya.')
                        tAlertSmoke = datetime.datetime.now()
                elif ((datetime.datetime.now()-tSmoke)>=delayUpdate) :
                        function.post("smoke",value)
                        tSmoke = datetime.datetime.now()
                

        if(str(msg.topic)=="lab/current"):
                value = str(msg.payload.decode("utf-8"))
                if ((datetime.datetime.now()-tDefault1)>=delayUpdate) :
                        function.post("current",value)
                        tDefault1 = datetime.datetime.now()

        if(str(msg.topic)=="lab/ldr"):
        #         print(type(msg.payload.decode("utf-8")))
                value = int(msg.payload.decode("utf-8"))
                if ((datetime.datetime.now()-tDefault2)>=delayUpdate):
                        function.post("ldr",value)
                        tDefault2 = datetime.datetime.now()



client.on_message = on_message
client.connect(server)
client.subscribe(topic)
client.loop_forever()
client.disconnect()