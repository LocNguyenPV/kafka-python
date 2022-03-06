import os
import requests
from urllib.parse import urljoin
from dotenv import load_dotenv
import json

load_dotenv()
API_URL = os.getenv("API_URL")
CREATE_DEVICE = urljoin(API_URL, 'createDevice')
# POST
headers_config = {
    'content-type': 'application/json',
   'Accept':'application/json',
    'connection': 'keep-alive',
    'Expect': '100-continue',
}
payload = json.dumps({"name": "loc_test_6"})
response = requests.post(CREATE_DEVICE, data=payload, headers=headers_config)
print(response.text)

# GET
response = requests.get(CREATE_DEVICE)
print(response.json()) # This method is convenient when the API returns JSON
