import requests

# fetch
resp = requests.get('<input URL.json>')

# print reponse as JSON
print(resp.json())
