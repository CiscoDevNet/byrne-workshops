#!/usr/bin/env python

'''

Copyright (c) {{current_year}} Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

'''

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://127.0.0.1:2225/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"

headers = {
    'Content-Type': "application/yang-data+json",
    'Accept': "application/yang-data+json",
    'Authorization': "Basic dmFncmFudDp2YWdyYW50",
    }

response = requests.request("GET", url, headers=headers, verify=False)

print(response.text)