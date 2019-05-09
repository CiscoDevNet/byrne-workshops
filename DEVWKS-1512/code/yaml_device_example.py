#! /usr/bin/env python3

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


