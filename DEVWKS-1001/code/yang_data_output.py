#!/usr/bin/env python

from ncclient import manager
import sys
import xml.dom.minidom


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

INT_FILTER = '''
                    <filter>
                        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                            <interface>
                                <name>GigabitEthernet2</name>
                            </interface>
                        <interface>
                                <name>GigabitEthernet3</name>
                            </interface>    
                        </interfaces>
                    </filter>
                  '''

def main():
    """
    Main method that prints netconf capabilities of remote device.
    """
    # Define a filter to restrict the amount of data coming back from the device

    # Create a NETCONF session to the router with ncclient
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:

        # Retrieve the configuraiton filtered as defined above
        results = m.get_config('running', INT_FILTER )
        # Print the output in a readable format
        print(xml.dom.minidom.parseString(results.xml).toprettyxml())
        acl_name = acl_desc["access-lists"]["access-list"]
        acl_match = acl_desc["access-lists"]["access-list"]["access-list-entries"]["access-list-entry"]




if __name__ == '__main__':
    sys.exit(main())



