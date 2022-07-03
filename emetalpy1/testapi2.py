#!/usr/bin/python3
import requests
import os
from pprint import pprint

token = os.getenv('TOKEN')
owner = "jotasantos"
repo = "python-net"
model_name = "users"
query_url = f"https://mockend.com/{owner}/{repo}/{model_name}?limit=0"
params = {
    "state": "open",
}
# headers = {'Authorization': f'token {token}'}
headers = {
'content-type': "application/json",
'x-auth-token':""
}
r = requests.get(query_url, headers=headers, params=params)
pprint(r.json())
