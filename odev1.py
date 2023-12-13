import requests
url = "https://coffee.alexflipnote.dev/random.json"
response = requests.get(url)
data = response.json()
print(data)