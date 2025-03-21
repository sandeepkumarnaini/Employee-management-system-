import requests
data={
    "username":"rama",
    "password":"krishna@123",
    "email":"krishna@gmail.com"
}
url='http://127.0.0.1:8000/api/register/'
resp=requests.post(url,json=data)
print(resp)
print(resp.json)
