#!/usr/bin/env python

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
                  <access-lists xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-acl-oper">
                    <access-list>
                      <access-control-list-name>CISCO_LIVE_IN</access-control-list-name>
                    </access-list>
                  </access-lists>
                  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <ip>
                      <access-list>
                        <extended xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-acl"/>
                      </access-list>
                    </ip>
                  </native>
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

        # Retrieve the configuraiton and operation data
        results = m.get(FILTER)



        # Print the raw XML Output
        print(xml.dom.minidom.parseString(results.xml).toprettyxml())

        acl_desc = xmltodict.parse(results.xml)["rpc-reply"]["data"]
        acl_conf = acl_desc["native"]["ip"]["access-list"]["extended"]["access-list-seq-rule"]
        acl_name = acl_desc["access-lists"]["access-list"]
        acl_match = acl_desc["access-lists"]["access-list"]["access-list-entries"]["access-list-entry"]

        print("Access-List Name: {}".format(acl_name["access-control-list-name"]["#text"]))
        for ace in acl_conf:

            try:
                print(" For ACE: {}".format(ace["sequence"]))
                print("  Protocol: {}".format(ace["ace-rule"]["protocol"]))
                host_ip = ace["ace-rule"]["ipv4-address"]
                print("   Host IP: {}".format(host_ip))
                print("   Wildcard Mask: {}".format(ace["ace-rule"]["mask"]))
                print("   Action: {}".format(ace["ace-rule"]["action"]))
            except KeyError:
                print("   Action: {}".format(ace["ace-rule"]["action"]))
            except Exception:
                print("  Cannot Understand ACE")

        for rule in acl_match:
            print(" For SEQ number: {}".format(rule["rule-name"])
                   + " the number of ACE matches is: {}".format(rule["access-list-entries-oper-data"]["match-counter"]))

if __name__ == '__main__':
    sys.exit(main())