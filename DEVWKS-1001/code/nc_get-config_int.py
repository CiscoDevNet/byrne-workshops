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

from ncclient import manager
import sys
import xml.dom.minidom
import xmltodict

# the variables below assume the user is leveraging the
# Vagrant image provided with the live delivery.  If running this
# as a self learning lab substitute your device details
# The IP address of your router/switch
HOST = '127.0.0.1'
# use the NETCONF port for your CSR1000V device
PORT = 2223
# use the user credentials for your CSR1000V device
USER = 'vagrant'
PASS = 'vagrant'

FILTER = '''
            <filter>
                <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                    <interface>
                        <name>GigabitEthernet2</name>
                    </interface>
                </interfaces>
            </filter>
         '''

def main():

    """
    Main method that prints netconf capabilities of remote device.
    """
    # Create a NETCONF session to the router with ncclient
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:

        # Retrieve the configuraiton
        results = m.get_config('running', FILTER)

        # Print the raw XML Output
        print(xml.dom.minidom.parseString(results.xml).toprettyxml())

        # Process teh XML and store the useful dictionaries
        intf_details = xmltodict.parse(results.xml)["rpc-reply"]["data"]
        intf_config = intf_details["interfaces"]["interface"]



        print("*******************************************************")
        print("Interface Details:")
        print("  Name: {}".format(intf_config["name"]["#text"]))
        print("  Description: {}".format(intf_config["description"]))
        print("  Type: {}".format(intf_config["type"]["#text"]))
        print("  Enabled: {}".format(intf_config["enabled"]))
        print("*******************************************************")


if __name__ == '__main__':
    sys.exit(main())