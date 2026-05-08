import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "reviews": "Worst product!"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())