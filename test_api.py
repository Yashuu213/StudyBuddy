import requests
import json

url = 'http://127.0.0.1:5000/api/generate_content'
data = {
    'topic_name': 'Electric Charges and Fields',
    'section': 'explanation'
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print("Response JSON:")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {e}")
