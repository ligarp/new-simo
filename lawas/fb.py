import json
import random
import serial
import datetime
from firebase import firebase
from urllib.request import urlopen


firebase = firebase.FirebaseApplication('https://websocket-dev.firebaseio.com/',None)
ser = serial.Serial('/dev/ttyACM0',9600)
def cek():
    try:
        response = urlopen('http://google.com',timeout=5)
        return (True)
    except Exception as e:
        return (False)

while True:
	if cek():
		try:
			arr = [ser.readline().decode("utf-8"),ser.readline().decode("utf-8")]
			now = datetime.datetime.now()
			result1 = firebase.post('/sensor/1',{'temperature' : str(arr[0]),'humidity' : str(arr[1]) , 'time' : str(now)})
			print (' suhu :', arr[0],'kelembabab :', arr[1], ' last update :', str(now))
		except Exception as e:
			pass
# result = firebase.get('/py/mahasiswa','')
# print (len(result))
# print (type(result))
print ('-------------------')
# print (result)
# print (result['-LNP5wk-NiA_s6anw1ff'])
# for i in range(len(result)):
#     print (result)
