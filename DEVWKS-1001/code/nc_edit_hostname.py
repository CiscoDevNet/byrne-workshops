#!/usr/bin/env python

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

        stage = m.get_config('running', FILTER)
        stage_desc = xmltodict.parse(stage.xml)["rpc-reply"]["data"]
        stage_conf = stage_desc["native"]
        print('****')
        print("The Original Hostname is: {}".format(stage_conf["hostname"]))
        print('****')
        print("Changing the Hostname Now")

        # Retrieve the configuraiton and operation data
        results = m.edit_config(PAYLOAD, target= 'running')
        print(results)

        verify = m.get_config('running', FILTER)
        verify_desc = xmltodict.parse(verify.xml)["rpc-reply"]["data"]
        verify_conf = verify_desc["native"]
        print('****')
        print("The New Hostname is: {}".format(verify_conf["hostname"]))
        print('****')

if __name__ == '__main__':
    sys.exit(main())