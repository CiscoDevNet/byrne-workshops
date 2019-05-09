#!/usr/bin/env python

from jinja2 import Template

device_details = [
    {'id': '101',
     'name': 'DATA',
     'desc': 'This is the SVI',
     'address': '10.0.10.1',
     'mask': '255.255.255.0'},
    {'id': '201',
     'name': 'VOICE',
     'desc': 'This is the VOICE SVI',
     'address': '10.0.20.1',
     'mask': '255.255.255.0'},
    {'id': '301',
     'name': 'GUEST',
     'desc': 'This is the GUEST SVI',
     'address': '10.0.30.1',
     'mask': '255.255.255.0'},
]

with open("jinja_loop.j2") as f:
    config_in = Template(f.read())

config_out = config_in.render(inputs=device_details)

print(config_out)
