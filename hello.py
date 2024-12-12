import requests

url = "https://rubah.pythonanywhere.com/add"
headers = {"Content-Type": "application/json"}
data = {
    "m": 8,
    "bits": 16,
    "type": "hex",
    "hex1": "001A",
    "hex2": "002B"
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Failed to get a valid response. Status code:", response.status_code)
    print("Response content:", response.text)
