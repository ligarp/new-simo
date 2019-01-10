from firebase import firebase
authentication = firebase.FirebaseAuthentication('e2ApT5zWI5VtmaqSEseX6JLglQSKlBgmFgwpyWDB', 'admin2@admin.com', extra={'password': 'admin123'})
firebaseapp = firebase.FirebaseApplication('https://websocket-dev.firebaseio.com', authentication=None)
firebase.authentication = authentication
# result = firebaseapp.get('/data', None)
print (authentication.get_user().firebase_auth_token)
result = firebaseapp.get('/data',authentication)
print (result)