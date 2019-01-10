import paho.mqtt.client as mqtt
import smsgateway
import function
username = "ragil"
password = "ragil"
topic = "lab/#"
server = "192.168.100.58"
client = mqtt.Client("client")
client.username_pw_set(username,password)

def on_connect(client, userdata, rc):
        print ("connected" + str(rc))
def on_message(client, userdata, msg):
        print("Topic :" + str(msg.topic))
        print("Message :" + str(msg.payload.decode("utf-8")))

        if(str(msg.topic)=="lab/pir"):
                
                if (msg.payload.decode("utf-8")=="0"):
                        value = "Tidak ada Aktifitas"
                elif (msg.payload.decode("utf-8")=="1"):
                        value = "Terdapat Aktifitas"
                else:
                        value = "Not Defined"
                function.put("pir",value)

        if(str(msg.topic)=="lab/temperature"):
                value = str(msg.payload.decode("utf-8"))
                function.put("temperature",value)

        if(str(msg.topic)=="lab/smoke"):
                # smsgateway.kirim_pesan("082220488112","Tingkat Asap: " + str(msg.payload.decode("utf-8")))
                # function.post("smoke",str(msg.payload.decode("utf-8")))
                function.put("smoke",str(msg.payload.decode("utf-8")))

        if(str(msg.topic)=="lab/current"):
                value = str(msg.payload.decode("utf-8"))
                function.put("current",value)

        if(str(msg.topic)=="lab/ldr"):
                print(type(msg.payload.decode("utf-8")))
                ldr = int(msg.payload.decode("utf-8"))
                if (ldr > 800):
                        value = "Sangat Terang"
                elif (ldr < 800 and ldr > 300):
                        value = "Normal"
                elif (ldr > 0 and ldr < 300):
                        value = "Redup/Mati"
                function.put("ldr",value)

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