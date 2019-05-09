#!/usr/bin/env python

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

