import paho.mqtt.client as mqtt
username = "ragil"
password = "ragil"
topic = "test"
server = "192.168.100.58"
client = mqtt.Client("client")
client.username_pw_set(username,password)

def on_connect(client, userdata, rc):
    print ("connected" + str(rc))
    client.subscribe(topic)
def on_message(client, userdata, msg):
    print("Topic :" + str(msg.topic))
    print("Message :" + str(msg.payload.decode("utf-8")))


client.on_message = on_message

client.connect(server)
client.subscribe(topic)
client.loop_forever()
client.disconnect()