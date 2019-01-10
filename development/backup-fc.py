from firebase import firebase
import datetime
import time
authentication = firebase.FirebaseAuthentication('e2ApT5zWI5VtmaqSEseX6JLglQSKlBgmFgwpyWDB', 'om.ragil7@gmail.com', extra={'id': 123})
firebase = firebase.FirebaseApplication('https://websocket-dev.firebaseio.com', authentication=None)
firebase.authentication = authentication
# user = authentication.get_user()
# print (user.firebase_auth_token)
def post(sensor,value):
    result = firebase.post('/data/'+sensor, {"value":value,"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    print (result)
    result_get = firebase.get('/data/'+sensor, str(result["name"]))
    print (result_get)
def put(sensor, value):
    # result = firebase.put('/data/realtime', {sensor+{"value":value,"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}})
    # print (result)
    tes = {"sensor":{"value":value,"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}}
    # print (({sensor+{"value":value,"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}}))
    print ({sensor:{"value":value,"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}})
    # result_get = firebase.get('/data/'+sensor, str(result["name"]))