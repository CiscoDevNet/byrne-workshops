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
from ncclient import manager, xml_
from jinja2 import Template
import yaml
import time
from argparse import ArgumentParser


# Setup and parse command line arguments for passing in hostname to CSR
parser = ArgumentParser("Setting the Router Hostname")
parser.add_argument(
    "-hn", "--hostname", help="This is the the hostname assigneed to the CSR", required=False, default="Router",
)

# Set up hostname variable to be used in NETCONF template
args = parser.parse_args()
rtr_hostname = args.hostname

# Read in the command_sets.yml file
with open("provision/command_sets_16_9.yml") as f:
    commands = yaml.load(f.read())["commands"]
    initial_config = commands["initial_config"]
    nat_vpg_config = commands["nat_config"]
    guestshell_config = commands["guestshell_config"]
    guestshell_enable = commands["guestshell_enable"]

# Read in the entire YAML file for use in various templates
print("Reading in Device Device Details")
with open("provision/device_details.yml") as f:
    device_details = yaml.load(f.read())

# Create the NETCONF template for creating interfaces
print("Setting Up NETCONF Templates")
with open("provision/templates/netconf_interface_template.j2") as f:
    interface_template = Template(f.read())

# Create the NETCONF template for configuring NAT
# The 'netconf_configs' directory must exist prior to running the script
# The template will not allow for configuring NAT inside on the VirtualPortGroup - Pushed via Netmiko
with open("provision/templates/netconf_nat_template_16_9.j2") as f:
    nat_template = Template(f.read())

# Create the NETCONF template for configuring NAT
# The 'netconf_configs' directory must exist prior to running the script
# The template will not allow for configuring NAT inside on the VirtualPortGroup - Pushed via Netmiko
with open("provision/templates/netconf_hostname_template.j2") as f:
    hostname_template = Template(f.read())

# Creating various .xml configuraitons
print("Creating Device Configurations")
for device in device_details["devices"]:
    print("Device: {}".format(device["name"]))

    # Creates interface .xml configuration
    print("Creating Interface Configurations from Templates")
    with open("provision/netconf_configs/{}_layer3.cfg".format(device["name"]), "w") as f:
        int_config = interface_template.render(interfaces=device["interfaces"])
        f.write(int_config)

    # Creates NAT .xml configuration
    print("Creating NAT Configurations from Templates")
    with open("provision/netconf_configs/{}_nat.cfg".format(device["name"]), "w") as f:
        nat_config = nat_template.render(nat=device["nat"])
        f.write(nat_config)

    # Creates hostname .xml configuration
    with open("provision/netconf_configs/{}_hostname.cfg".format(device["name"]), "w") as f:
        hostname_config = hostname_template.render(hostname=rtr_hostname)
        f.write(hostname_config)

# Creating session details to be used by ncclient to set the hostname. The intention is to reuse 'm' for calling ncclient sessions.
# The hostname needs to be set before making any configuration changes with netmiko.
# Netmiko expects the original hostname in the reponse.

for device in device_details["devices"]:
    print("Defining netmiko session details on DEVICE: {}".format(device["name"]))

    with manager.connect(host=device["ip"],
                         username=device["username"],
                         password=device["password"],
                         port=device["netconf_port"],
                         allow_agent=False,
                         look_for_keys=False,
                         hostkey_verify=False) as m:

        # Sending hostname configurations to the router via NETCONF
        print("Sending hostname Configuration with Ncclient")
        hostname_resp = m.edit_config(hostname_config, target='running')

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
        print("Pausing 75 seconds for NETCONF to Start on Router")
        time.sleep(75)

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

        # Configuring Guestshell via CLI
        print("Sending Guestshell Config Netmiko")
        guestshell_resp = ch.send_config_set((guestshell_config))

        # Enabling Guestshell
        print("Enabling Guestshell Netmiko")
        enable_gs_resp = ch.send_command((guestshell_enable))

        # Installing git in the IOS-XE Guestshell
        print("Installing git in guestshell")
        guestshell_git_resp = ch.send_command("guestshell run sudo yum install -y git")

        # Updating some of the core Linux packages libraries. Without these
        # updates guestshell is unable to clone repo
        print("Updating nss, curl, and libcurl")
        guestshell_update_resp = ch.send_command("guestshell run sudo yum update -y nss curl libcurl")

        # Cloing the git repo for DEVWKS-2556
        print("Cloning rshoemak/DevNet2556 to the guestshell")
        guestshell_clone_resp = ch.send_command("guestshell run git clone https://github.com/rshoemak/DevNet2556")

        # Executing a shell script in the guestshell to prepare the environment
        print("Executing the shell script for provisioning the guestshell")
        guestshell_shell_resp = ch.send_command("guestshell run ./DevNet2556/laptop-prep.sh")

        # File copy confirmation must be disabled. Otherwise netmiko gets an unexpected response
        # and the script fails.
        print("Disable copy prompts in IOS")
        guestshell_silent_resp = ch.send_config_set("file prompt quiet")

        # Copying router configurations needed for DEVWKS-2556
        print("Copying additional router configurations")
        guestshell_copy_resp = ch.send_command("copy bootflash:IOS-config-base.txt running-config")

        # Re-enabling copy prompts in IOS
        print("Enable copy prompts in IOS")
        guestshell_alert_resp = ch.send_config_set("file prompt alert")

        # Quick validation to ensure that the correct interfaces have been configured
        # There should be 5 total interfaces including 3 Gig3, 1 Loop, and 1 VPG
        guestshell_ship_resp = ch.send_command("show ip int bri")
        print("************************************************************************")
        print(guestshell_ship_resp)
        print("************************************************************************")


# Saving the router configuration
with manager.connect(host=device["ip"],
                     username=device["username"],
                     password=device["password"],
                     port=device["netconf_port"],
                     allow_agent=False,
                     look_for_keys=False,
                     hostkey_verify=False) as m:
    save_body = '<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>'

    # Send the RPC to the Device
    save_rpc = m.dispatch(xml_.to_ele(save_body))

    # Confirm Config Save
    print('**************************************************')
    print()
    print(save_rpc)
    print()
    print('**************************************************')








