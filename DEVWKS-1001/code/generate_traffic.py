#! /usr/bin/env python3

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


with ConnectHandler(device_type='cisco_ios',
                    ip=HOST,
                    username=USER,
                    password=PASS,
                    port=PORT) as ch:

    ping_gdns = ch.send_command("ping 8.8.8.8 repeat 10")
    ping_odns = ch.send_command("ping 208.67.222.222 repeat 200")

    print(ping_gdns)
    print(ping_odns)


