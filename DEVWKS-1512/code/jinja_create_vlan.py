#!/usr/bin/env python

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
