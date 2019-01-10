# from google.oauth2 import service_account
# from google.auth.transport.requests import AuthorizedSession
# import google.auth.transport.requests
# import urllib3
# import json
# import datetime
# http = urllib3.PoolManager()

# # Define the required scopes
# scopes = [
#   "https://www.googleapis.com/auth/userinfo.email",
#   "https://www.googleapis.com/auth/firebase.database"
# ]

# # Authenticate a credential with the service account
# credentials = service_account.Credentials.from_service_account_file(
#     "/app/python/websocket-dev-firebase-adminsdk-bz46i-27de4a9269.json", scopes=scopes)

# # Use the credentials object to authenticate a Requests session.
# authed_session = AuthorizedSession(credentials)
# response = authed_session.get(
#     "https://websocket-dev.firebaseio.com/data.json")

# # Or, use the token directly, as described in the "Authenticate with an
# # access token" section below. (not recommended)
# request = google.auth.transport.requests.Request()
# credentials.refresh(request)
# access_token = credentials.token

import time
def pesan():
    r = http.request('GET', 'https://websocket-dev.firebaseio.com/data.json?access_token='+access_token)
    print (r.status)
    print (json.loads(r.data))
def post(sensor,time,value):
    from google.oauth2 import service_account
    from google.auth.transport.requests import AuthorizedSession
    import google.auth.transport.requests
    import urllib3
    import json
    import datetime
    http = urllib3.PoolManager()

    # Define the required scopes
    scopes = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/firebase.database"
    ]

    # Authenticate a credential with the service account
    credentials = service_account.Credentials.from_service_account_file(
        "/app/python/websocket-dev-firebase-adminsdk-bz46i-27de4a9269.json", scopes=scopes)

    # Use the credentials object to authenticate a Requests session.
    authed_session = AuthorizedSession(credentials)
    response = authed_session.get(
        "https://websocket-dev.firebaseio.com/data.json")

    # Or, use the token directly, as described in the "Authenticate with an
    # access token" section below. (not recommended)
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)
    access_token = credentials.token
    data ={"time": time,"value": value}
    encoded_data = json.dumps(data).encode('utf-8')
    r = http.request('POST', 'https://websocket-dev.firebaseio.com/data/'+sensor+'.json?access_token='+access_token,
        body=encoded_data)
value = str(10)
# post('arus',str(datetime.datetime.now()),value)
