#! /usr/bin/env python3

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

import yaml
from pprint import pprint

print("Reading in Device Device Details")
with open("yaml_device_example.yaml") as f:
    device_details = yaml.safe_load(f.read())

for line in device_details["devices"]:
    print()
    pprint("***************************************")
    pprint("For device:  {}" .format(line["name"]))
    pprint("***************************************")
    pprint(line)
    print()


