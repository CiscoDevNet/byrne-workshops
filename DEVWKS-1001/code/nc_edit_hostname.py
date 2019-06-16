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
                  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <hostname></hostname>
                  </native>
                </filter>
            '''

PAYLOAD = '''
                <config>
                  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <hostname>Cisco_Live_2019</hostname>
                  </native>
                </config>
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

        # Use ncclient to retrieve the configuration matching the defined filter. Parse output.
        stage = m.get_config('running', FILTER)
        stage_desc = xmltodict.parse(stage.xml)["rpc-reply"]["data"]
        stage_conf = stage_desc["native"]
        print('****')
        print("The Original Hostname is: {}".format(stage_conf["hostname"]))
        print('****')
        print("Changing the Hostname Now")

        # Use ncclient to modify the configuration with the defined XML data.
        results = m.edit_config(PAYLOAD, target= 'running')
        print(results)

        # Use ncclient to verify the changes were applied.
        verify = m.get_config('running', FILTER)
        verify_desc = xmltodict.parse(verify.xml)["rpc-reply"]["data"]
        verify_conf = verify_desc["native"]
        print('****')
        print("The New Hostname is: {}".format(verify_conf["hostname"]))
        print('****')

if __name__ == '__main__':
    sys.exit(main())
