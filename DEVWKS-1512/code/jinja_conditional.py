#!/usr/bin/env python

"""

Copyright (c) 2019 Cisco and/or its affiliates.

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

"""

__author__ = "Bryan Byrne <brybyrne@cisco.com>"
__contributors__ = [
]
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"

from jinja2 import Template

device_details = [
    {'mode': 'trunk',
     'interface': 'GigabitEthernet 0/24',
     'allowed': '10,20,30-35',
     'vlan': '',
     'address': '',
     'mask': '',
     'enabled': 'true'},
    {'mode': 'access',
     'interface': 'GigabitEthernet 0/2',
     'allowed': '',
     'vlan': '10',
     'address': '',
     'mask': '',
     'enabled': 'true'},
    {'mode': 'access',
     'interface': 'GigabitEthernet 0/3',
     'allowed': '',
     'vlan': '20',
     'address': '',
     'mask': '',
     'enabled': 'false'},
    {'mode': 'routed',
     'interface': 'GigabitEthernet 0/1',
     'allowed': '',
     'address': '10.10.20.1',
     'mask': '255.255.255.252',
     'enabled': 'true'},
]

with open("jinja_conditional.j2") as f:
    config_in = Template(f.read())

config_out = config_in.render(inputs=device_details)

print(config_out)

