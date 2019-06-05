## Module 1 Exercise: Working iwth YAML Data

Before we start the lab let's make sure we are in the correct code directory.

```
cd DEVWKS-1512/code
```

#### Task 1 - A Brief Primer on YAML

In this example we will read a YAML file into some code and print the output. While not overly compelling compared to a network automation script it's important to understand how we can import YAML data into our code.

First let's look at the YAML file we will be working with.

Type or Paste:

```
cat yaml_device_example.yaml
```

The output will look similar to the following:

```
---
devices:

  - name: rtr_1
    mgmt_ip: '10.10.10.10'
    username: 'rtr1_user'
    password: 'shh_secret'
    interfaces:
      - name: GigabitEthernet1
        enabled: "true"
        description: "Connected to RTR 1"
        ip: 192.168.35.1
        subnet: 255.255.255.252
      - name: GigabitEthernet2
        enabled: "false"
        description: "To User Segment"
        ip: 172.20.16.1
        subnet: 255.255.255.0
      - name: Loopback 100
        enabled: "true"
        description: "OSPF RID"
        ip: 10.255.255.1
        subnet: 255.255.255.255
  - name: rtr_2
    mgmt_ip: '20.20.20.20'
    username: 'rtr2_user'
    password: 'shh_secret'
    interfaces:
      - name: GigabitEthernet1
        enabled: "true"
        description: "Connected to RTR 1"
        ip: 192.168.35.2
        subnet: 255.255.255.252
      - name: GigabitEthernet2
        enabled: "true"
        description: "To User Segment"
        ip: 172.20.16.1
        subnet: 255.255.255.0
      - name: Loopback 100
        enabled: "true"
        description: "OSPF RID"
        ip: 10.255.255.2
```

First it's important to note that a YAML file will start with three dashes '---'. If we think back to the previous section we should be able to identify our lists and dictionaries.

- The file starts out with a dictionary with a key of 'devices'. The devices key contain two list instances (rtr_1 and rtr2).
- Each list instance for our routers contain a number of key:value pairs
	- management IP address
	- username
	- password
	- A nested dictionary containing a list of interfaces.

Now let's take a look at the Python code.

```
cat yaml_device_example.py
```

The code should look similar to this:

```
import yaml
from pprint import pprint

print("Reading in Device Device Details")
with open("yaml_device_example.yaml") as f:
    device_details = yaml.safe_load(f.read())

for line in device_details["devices"]:
    print()
    pprint("***************************************")
    pprint("For device:  {}" .format(line["name"]))
    pprint("***************************************")
    pprint(line)
    print()
```

- First we need to bring in the YAML library. We do this with 'import yaml'
- Next we need to read in the YAML file and assign it to a variable. In my example I open the file and assign a variable of f. Then we use a function from the yaml library 'safe-load'
	- It's important to note that using the 'load' function rather than 'safe-load' leads to the potential to import code and have it arbitrarily executed. The use of 'safe-load' prevents remote code execution and is just a good habit to form.
- After we load in the YAML details and assign it to the device_details variable.
- Now we print the output.
	- Note that when we read in the YAML structured data I can extract portions of the data similar to any list or dictionary. 

Let's run the code. Type or Paste:

```
python yaml_device_example.py
```

The output:

```
'***************************************'
'For device:  rtr_1'
'***************************************'
{'interfaces': [{'description': 'Connected to RTR 1',
                 'enabled': 'true',
                 'ip': '192.168.35.1',
                 'name': 'GigabitEthernet1',
                 'subnet': '255.255.255.252'},
                {'description': 'To User Segment',
                 'enabled': 'false',
                 'ip': '172.20.16.1',
                 'name': 'GigabitEthernet2',
                 'subnet': '255.255.255.0'},
                {'description': 'OSPF RID',
                 'enabled': 'true',
                 'ip': '10.255.255.1',
                 'name': 'Loopback 100',
                 'subnet': '255.255.255.255'}],
 'mgmt_ip': '10.10.10.10',
 'name': 'rtr_1',
 'password': 'shh_secret',
 'username': 'rtr1_user'}


'***************************************'
'For device:  rtr_2'
'***************************************'
{'interfaces': [{'description': 'Connected to RTR 1',
                 'enabled': 'true',
                 'ip': '192.168.35.2',
                 'name': 'GigabitEthernet1',
                 'subnet': '255.255.255.252'},
                {'description': 'To User Segment',
                 'enabled': 'true',
                 'ip': '172.20.16.1',
                 'name': 'GigabitEthernet2',
                 'subnet': '255.255.255.0'},
                {'description': 'OSPF RID',
                 'enabled': 'true',
                 'ip': '10.255.255.2',
                 'name': 'Loopback 100',
                 'subnet': '255.255.255.255'}],
 'mgmt_ip': '20.20.20.20',
 'name': 'rtr_2',
 'password': 'shh_secret',
 'username': 'rtr2_user'}
```

So with a basic understanding of YAML let's move on to looking at Jinja Templating.

## [Module 2: Jinja Templating](DEVWKS_1512_4.md)
## [Return to the Table of Contents](../../README.md)