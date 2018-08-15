import requests

req = requests.get('https://api.darksky.net/forecast/aa8cc6f74c378224fedde5330003b8f2/38,-122',stream = True)

print(req.text)