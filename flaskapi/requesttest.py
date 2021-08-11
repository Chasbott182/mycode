import flaskapi03
import requests

for x in range(1,51):
    response = requests.get("http://192.168.18.43:3000/user/Chas")
    print(response)