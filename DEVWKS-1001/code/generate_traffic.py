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

from netmiko import ConnectHandler

# the variables below assume the user is leveraging the
# Vagrant image provided with the live delivery.  If running this
# as a self learning lab substitute your device details
# The IP address of your router/switch
HOST = '127.0.0.1'
# use the SSH port for your CSR1000V device
PORT = 2222
# use the user credentials for your CSR1000V device
USER = 'vagrant'
PASS = 'vagrant'

# Define netmiko session details and send ping command to router.
with ConnectHandler(device_type='cisco_ios',
                    ip=HOST,
                    username=USER,
                    password=PASS,
                    port=PORT) as ch:

    ping_gdns = ch.send_command("ping 8.8.8.8 repeat 10")
    ping_odns = ch.send_command("ping 208.67.222.222 repeat 200")

    print(ping_gdns)
    print(ping_odns)


