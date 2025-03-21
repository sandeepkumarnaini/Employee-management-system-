import requests
crediantials={
    "username":"rama",
    "password":"krishna@123"
}
url='http://127.0.0.1:8000/api/login/'
resp=requests.post(url,json=crediantials)
print(resp)
#print(resp.json())
tkn=resp.json()['token']
get_url='http://127.0.0.1:8000/api/'
resp=requests.get(get_url,headers={
    'Authorization':'Token {}'.format(tkn)})
print(resp)
print(resp.json())
