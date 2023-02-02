#!/usr/bin/python
'''
This is the code for gathering all possible domains of the organization.
you can automate this with httpx to get live domains. Have Fun
'''
import requests, json, sys
target = sys.argv[1].rstrip()

req = requests.get("https://crt.sh/?q=%.{d}&output=json".format(d=target))
json_data = json.loads(req.text)
for (key,value) in enumerate(json_data):
    print(value['common_name'])
