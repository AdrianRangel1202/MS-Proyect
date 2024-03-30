import requests




url = "http://127.0.0.1:8000/users/post_user"
data = {
    "username":"Marcos",
    "email":"Marcost12@gmail.com",
    "password": "123145",
}
response = requests.post(url, data=data)

print(response.json())