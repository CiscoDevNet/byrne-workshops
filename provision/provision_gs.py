#! /usr/bin/env python3

"""

Copyright (c) 2018 Cisco and/or its affiliates.

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
    "Hank Preston <hapresto@cisco.com>",
]
__copyright__ = "Copyright (c) 2018 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"

from netmiko import ConnectHandler
from ncclient import manager
from jinja2 import Template
import yaml
import time


# Read in the command_sets.yml file
with open("command_sets.yml") as f:
    commands = yaml.load(f.read())["commands"]
    initial_config = commands["initial_config"]
    nat_vpg_config = commands["nat_config"]
    guestshell_config = commands["guestshell_config"]
    guestshell_enable = commands["guestshell_enable"]

# Read in the entire YAML file for use in various templates
print("Reading in Device Device Details")
with open("device_details.yml") as f:
    device_details = yaml.load(f.read())

# Create the NETCONF template for creating interfaces
print("Setting Up NETCONF Templates")
with open("templates/netconf_interface_template.j2") as f:
    interface_template = Template(f.read())

# Create the NETCONF template for configuring NAT
# The 'netconf_configs' directory must exist prior to running the script
# The template will not allow for configuring NAT inside on the VirtualPortGroup - Pushed via Netmiko
with open("templates/netconf_nat_template.j2") as f:
    nat_template = Template(f.read())

# Creating various .xml configuraitons
print("Creating Device Configurations")
for device in device_details["devices"]:
    print("Device: {}".format(device["name"]))

    # Creates interface .xml configuration
    print("Creating Interface Configurations from Templates")
    with open("netconf_configs/{}_layer3.cfg".format(device["name"]), "w") as f:
        int_config = interface_template.render(interfaces=device["interfaces"])
        f.write(int_config)

    # Creates NAT .xml configuration
    print("Creating NAT Configurations from Templates")
    with open("netconf_configs/{}_nat.cfg".format(device["name"]), "w") as f:
        nat_config = nat_template.render(nat=device["nat"])
        f.write(nat_config)

# Creating session details to be used by Netmiko. The intention is to reuse 'ch' for calling Netmiko sessions.
for device in device_details["devices"]:
    print("Defining netmiko session details on DEVICE: {}".format(device["name"]))

    with ConnectHandler(device_type=device["device_type"],
                        ip=device["ip"],
                        username=device["username"],
                        password=device["password"],
                        port=device["ssh_port"]) as ch:

        # Configuring NETCONF/RESTCONF with Netmiko
        print("Sending Initial Configuration with Netmiko")
        initial_resp = ch.send_config_set(initial_config)

        # Just pausing the script waiting for NETCONF to start
        print("Pausing 45 seconds for NETCONF to Start on Router")
        time.sleep(45)

        print("Defining netconf session details on DEVICE: {}".format(device["name"]))

        with manager.connect(host=device["ip"],
                             username=device["username"],
                             password=device["password"],
                             port=device["netconf_port"],
                             allow_agent=False,
                             look_for_keys=False,
                             hostkey_verify=False) as m:

            # Sending interface configurations to the router via NETCONF
            print("Sending Interface Configuration with Ncclient")
            interface_resp = m.edit_config(int_config, target = 'running')

            # Without this sleep timer the remote device kicks back a an RPC error
            print("Pausing 5 seconds for Ncclient")
            time.sleep(5)

            # Sending NAT configurations to the router via NETCONF
            print("Sending NAT Configuration with Ncclient")
            nat_resp = m.edit_config(nat_config, target = 'running')

        # Sending CLI command to configure 'ip nat inside' on VirtualPortGroup due to lack of YANG model support
        print("Sending Additional NAT Config with Netmiko")
        nat_vpg_resp = ch.send_config_set((nat_vpg_config))

        # Configuring Guestshell via CLI
        print("Sending Guestshell Config Netmiko")
        guestshell_resp = ch.send_config_set((guestshell_config))

        # Enabling Guestshell
        print("Enabling Guestshell Netmiko")
        enable_gs_resp = ch.send_command((guestshell_enable))

