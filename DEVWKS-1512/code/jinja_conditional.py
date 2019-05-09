#!/usr/bin/env python

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

