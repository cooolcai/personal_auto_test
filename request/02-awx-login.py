import requests
url_login = "http://10.20.3.148:31426/api/login/"
data = {"username": "admin",
        "password": "b3KhU0QDKj5gdnjfkQ4hgNk3WSWpPaCU",
        }
r = requests.post(url=url_login, data=data)
print(r.url)
print(r.status_code)
print(r.json())