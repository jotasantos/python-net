#!/usr/bin/python3.6

import requests
import json
import ipaddress

fp = open ('backend_results.json', "r")

# Reading from file
data = json.loads(fp.read())
# Now json is in data variable
#print (json.dumps(data["response"], indent=2))
response = data["response"]

dict_result = {}
for res in response:
 server = res["attributes"]["display_name"]
 ip = res["attributes"]["private_ip_0"]

 an_address = ipaddress.ip_address(ip)
 a_network = ipaddress.ip_network('10.33.64.0/19')
 if an_address in a_network:
   print(res["attributes"]["display_name"])
   print(res["attributes"]["private_ip_0"])


 
