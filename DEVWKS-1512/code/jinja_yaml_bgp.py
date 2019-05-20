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
import yaml

print("Reading in Device Device Details")
with open("jinja_yaml_bgp.yaml") as f:
    device_details = yaml.safe_load(f.read())

with open("jinja_yaml_bgp.j2") as f:
    template_in = Template(f.read())

for device in device_details["devices"]:
    print("***** Generating Configuration for: {} *****".format(device["name"]))
    template_out = template_in.render(name=device["name"],asn=device["asn"], rid=device["rid"], neighbor=device["neighbor"])

    print(template_out)

