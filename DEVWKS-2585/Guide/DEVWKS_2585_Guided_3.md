## Module 2: Working with RESTCONF Operations

#### Task 4 - Retreiving Device Details with GET

```
https://{{host}}:{{port}}/restconf/data/ietf-interfaces:interfaces-state/interface=GigabitEthernet1
```

#### Task 5 - Creating an Interface with POST
URI:

```
https://{{host}}:{{port}}/restconf/data/ietf-interfaces:interfaces/
```
Body:

```
{
  "ietf-interfaces:interface": {
    "name": "Loopback100",
    "description": "**Created at CLUS 2019**",
    "type": "iana-if-type:softwareLoopback"
	}
}
```

Verfify:

```
https://{{host}}:{{port}}/restconf/data/ietf-interfaces:interfaces/interface=Loopback100
```

#### Task 6: Updating a Device with PUT

URI:

```
https://{{host}}:{{port}}/restconf/data/ietf-interfaces:interfaces/interface=Loopback100/ietf-ip:ipv4/
```
Body:

```
{
    "ietf-ip:ipv4": {
        "address": [
            {
                "ip": "10.20.30.1",
                "netmask": "255.255.255.255"
            }
        ]
    }
}
```

Verfify:

```
https://{{host}}:{{port}}/restconf/data/ietf-interfaces:interfaces/interface=Loopback100
```


## [Moving on to the Bonus Content!](DEVWKS_2585_Guided_4.md)
## [Return to the Table of Contents](../../README.md)