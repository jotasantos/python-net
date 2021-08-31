#!/usr/bin/python3.6

import requests
import json

#region=""
region = "&region=uk-london-1"
#region = "&region=eu-amsterdam-1"
#region = "&region=eu-frankfurt-1"
#region = "&region=iad"
#region = "&region=ap-sydney-1"
#region = "&region=us-phoenix-1"

url = "https://folsom.whatevercloud.com/folsom/instance?compartment_id=ocid1.compartment.oc1..aaaaaaaalnhfd3hp5clfkbn2wjj3h3gysjct6fjtzbc7c5lvjdfs62gjtllq" + region

payload = {}
headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyMzkyNDk5NiwianRpIjoiZTQ1MGVjNDItZWIzNi00NmU5LWJiM2UtMmU3YzEwNmFiZTFjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImphaW1lLnNhbnRvcy5hbWFuZGkiLCJuYmYiOjE2MjM5MjQ5OTZ9.0mvzetI2Te-flyKCVkarqi0Yv-AgMiOG7UKGZMdVseQ'
}

response = requests.get(url, headers=headers, data=payload)
# Convert the api response to dictionary and store it
json_data = response.json()
with open("backend_results.json", "w") as fp:
    json.dump(json_data,fp) 

