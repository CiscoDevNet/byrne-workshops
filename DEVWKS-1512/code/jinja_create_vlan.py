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

from jinja2 import Template

template_in = Template("""
            vlan {{ id }}
             name {{vlan_name }}
            !
            interface vlan {{ id }}
             ip address {{ ip_addr }} {{ mask }}
             """)

template_out = template_in.render(id=200,
                                  vlan_name='DATA',
                                  ip_addr='192.168.1.1',
                                  mask="255.255.255.0")

print(template_out)
