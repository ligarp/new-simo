from firebase import firebase
from pyfcm import FCMNotification
import datetime
import time
import urllib3
import json
from urllib.request import urlopen

authentication = firebase.FirebaseAuthentication('e2ApT5zWI5VtmaqSEseX6JLglQSKlBgmFgwpyWDB', 'om.ragil7@gmail.com', extra={'id': 123})
firebase = firebase.FirebaseApplication('https://websocket-dev.firebaseio.com', authentication=None)
firebase.authentication = authentication
def cek():
    try:
        response = urlopen("http://google.com",timeout=5)
        return (True)
    except Exception as e:
        return (False)
# user = authentication.get_user()
# print (user.firebase_auth_token)
def post(sensor,value):
    try:
        if cek():
            firebase.post('/data/'+sensor, {"value":value,"time": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))})
            print ("Sukses : "+sensor)
            
            
        else:
            pass
    except Exception as e:
        pass
    # result_get = firebase.get('/data/'+sensor, str(result["name"]))
    # print (result_get)
def put(sensor, value):
    # result = firebase.put('/realtime', {sensor+{"value":value,"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}})
    # print (result)
    # tes = {"sensor":{"value":value,"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}}
    # print (({sensor+{"value":value,"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}}))
    # print ({sensor:{"value":value,"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}})
    try:
        if cek():
            firebase.put("/realtime", sensor ,{"value":value,"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    except Exception as e:
        pass
    
    # result_get = firebase.get('/data/'+sensor, str(result["name"]))

def pesan(no,pesan):
    http = urllib3.PoolManager()
    urllib3.disable_warnings()
    data ={"Content":{"phone_number": str(no),"message": "[SIMO] - " + str(pesan),"device_id": 107132}}
    encoded_data = json.dumps(data).encode('utf-8')
    r = http.request('POST', 'https://smsgateway.me/api/v4/message/send', headers={
        'Authorization' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTU0NTM5ODEwNCwiZXhwIjo0MTAyNDQ0ODAwLCJ1aWQiOjY1NjAwLCJyb2xlcyI6WyJST0xFX1VTRVIiXX0.M8wJhfR6RZ7WrELcFtM9AhTiW1ta4w7QgdCIHAVp6Zc','Content-Type': 'application/json'},
        body=encoded_data)
    print (r.status)
    print (json.loads(r.data))

def notif(message):
    push_service = FCMNotification(api_key="AAAA_mCm21w:APA91bGSUlb9rJ_A8Fi92Jcl_HEYlZduYaflPFq7lyx4akePCnuOdkmcu0ia9Yc0w7FuEtXNx7CMBERA1p-OMnA_2NZ-DPVaEJwhrtlKvdctBYxdEiJm-78-8B4nkXa4UmrjOsvZC45l")
    result = result = push_service.notify_topic_subscribers(topic_name="simo-client-android", message_body=message)

notif("tes")