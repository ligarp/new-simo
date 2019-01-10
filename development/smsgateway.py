import time
import urllib3
import json
def pesan(no,pesan):
    http = urllib3.PoolManager()
    data ={"Content":{"phone_number": str(no),"message": str(pesan),"device_id": 107132}}
    encoded_data = json.dumps(data).encode('utf-8')
    r = http.request('POST', 'https://smsgateway.me/api/v4/message/send', headers={
        'Authorization' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTU0NTM5ODEwNCwiZXhwIjo0MTAyNDQ0ODAwLCJ1aWQiOjY1NjAwLCJyb2xlcyI6WyJST0xFX1VTRVIiXX0.M8wJhfR6RZ7WrELcFtM9AhTiW1ta4w7QgdCIHAVp6Zc','Content-Type': 'application/json'},
        body=encoded_data)
    print (r.status)
    print (json.loads(r.data))
def kirim_pesan(nomer,isi_pesan):
    time.sleep(5)
    pesan(nomer,'[Simo]--'+ str(isi_pesan))
